from logic.barcode import manual_input, camera_input
from logic.nutrition import get_product


choice = input("Choose input method (manual/camera): ")

if choice == "manual":
    barcode = manual_input()

elif choice == "camera":
    barcode = camera_input()

else:
    print("Invalid input method.")
    exit()


product = get_product(barcode)


if product is None:
    print("Product not found.")
else:
    print("----- PRODUCT -----")
    print("Name:", product["name"])
    print("Brand:", product["brand"])
    print("Barcode:", product["barcode"])

    print("\n----- PRODUCT SIZE -----")
    print("Package:", product["package_quantity"], product["package_unit"])
    print("Serving:", product["serving_quantity"], product["serving_unit"])

    print("\n----- NUTRITION PER SERVING -----")
    print("Calories:", product["calories"])
    print("Protein:", product["protein"])
    print("Carbs:", product["carbs"])
    print("Sugar:", product["sugar"])
    print("Fat:", product["fat"])
    print("Saturated fat:", product["saturated_fat"])
    print("Fiber:", product["fiber"])
    print("Salt:", product["salt"])