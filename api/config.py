"""Expose only the public Supabase connection settings to the browser."""

import json
import os
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_PUBLISHABLE_KEY") or os.environ.get("SUPABASE_KEY")
        if not url or not key:
            self._send_json(503, {"error": "Supabase is not configured. Set SUPABASE_URL and SUPABASE_PUBLISHABLE_KEY (or SUPABASE_KEY)."})
            return
        if not key.startswith("sb_publishable_"):
            self._send_json(500, {"error": "The Supabase key must be a publishable key (sb_publishable_…). Do not use a secret or service-role key."})
            return

        self._send_json(200, {"url": url, "publishableKey": key})

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
