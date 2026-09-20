import requests

#Main URL
data_url = "https://world.openfoodfacts.org/api/v2/product/"

#barcode -> ATM manual placeholder, will see how to integrate actual barcode scanning
barcode = input("Insert the barcode here: ")
url = f"{data_url}{barcode}"
print(f"The URL produced is: {url} \n PLEASE LOOK HERE")

#https://openfoodfacts.github.io/documentation/docs/Product-Opener/v2/products/get-product-by-code/?utm_source=chatgpt.com
request_info = {
    "User-Agent": "Calorie_tracker_project(test@email.com)"
}

response = requests.get(url, headers=request_info)

if response.status_code == 200:
    data = response.json()

    #The actual product information
    product = data["product"]

    #basic information
    print("----- PRODUCT-----")
    print(f"Name: {product.get('product_name', 'Unknown')}")
    print(f"Brand: {product.get('brands', 'Unknown')}")
    print(f"Barcode: {product.get('code', barcode)}")

    #cateogries
    print("-----Categories-----")

    main_category = product.get("pnns_groups_1", "Unknown")
    sub_category = product.get("pnns_groups_2", "Unknown")

    #detailed categories
    print("-----Detailed Categories-----")

    categories = product.get("categories_hierarchy", [])

    for category in categories:
    # Remove the language prefix, e.g. "en:fruit-juices"
        category_name = category.split(":", 1)[-1]

        # Make it easier to read
        category_name = category_name.replace("-", " ").title()

        print(f"- {category_name}")

    #nutirition facts
    nutriments = product.get("nutriments", {})

    print("-----Nutrients-----")

    print("Calories:", nutriments.get("energy-kcal_100g"))
    print("Protein:", nutriments.get("proteins_100g"))
    print("Carbs:", nutriments.get("carbohydrates_100g"))
    print("Sugar:", nutriments.get("sugars_100g"))
    print("Fat:", nutriments.get("fat_100g"))
    print("Saturated fat:", nutriments.get("saturated-fat_100g"))
    print("Fiber:", nutriments.get("fiber_100g"))
    print("Salt:", nutriments.get("salt_100g"))

else:
    print(f"Something went wrong. Status code: {response.status_code}")