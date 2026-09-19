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
    print(data)

    #USED FOR: saving the information into a txt file
    #with open("test.txt", "w") as f:
        #f.write(str(data))

else:
    print(f"Something went wrong. Status code: {response.status_code}")