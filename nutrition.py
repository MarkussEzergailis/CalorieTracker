import requests


def get_product(barcode):

    data_url = "https://world.openfoodfacts.org/api/v2/product/"
    url = f"{data_url}{barcode}"

    request_info = {
        "User-Agent": "Calorie_tracker_project(test@email.com)"
    }

    response = requests.get(url, headers=request_info)

    if response.status_code != 200:
        return None

    data = response.json()
    product = data["product"]

    nutriments = product.get("nutriments", {})

    product_quantity = product.get("product_quantity")
    product_unit = product.get("product_quantity_unit")

    serving_quantity = product.get("serving_quantity")
    serving_unit = product.get("serving_quantity_unit")

    return {
        "name": product.get("product_name", "Unknown"),
        "brand": product.get("brands", "Unknown"),
        "barcode": product.get("code", barcode),

        "package_quantity": product_quantity,
        "package_unit": product_unit,

        "serving_quantity": serving_quantity,
        "serving_unit": serving_unit,

        "calories": nutriments.get("energy-kcal_serving"),
        "protein": nutriments.get("proteins_serving"),
        "carbs": nutriments.get("carbohydrates_serving"),
        "sugar": nutriments.get("sugars_serving"),
        "fat": nutriments.get("fat_serving"),
        "saturated_fat": nutriments.get("saturated-fat_serving"),
        "fiber": nutriments.get("fiber_serving"),
        "salt": nutriments.get("salt_serving")
    }