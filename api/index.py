import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

from logic.nutrition import get_product


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        barcode = parse_qs(urlparse(self.path).query).get("barcode", [""])[0].strip()

        if not barcode or not barcode.isdigit():
            self._send_json(400, {"error": "Provide a numeric barcode in the barcode query parameter."})
            return

        try:
            product = get_product(barcode)
        except Exception:
            self._send_json(502, {"error": "The product lookup service is currently unavailable."})
            return

        if product is None:
            self._send_json(404, {"error": "Product not found."})
            return

        self._send_json(200, product)

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
