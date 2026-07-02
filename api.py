#api
import requests

BASE_URL = "https://world.openfoodfacts.net/api/v2/product/{product_name}"

def search_product(product_name):
    url = BASE_URL.format(product_name=product_name)

    response = requests.get(url)

    if response.status_code == 200: #successful response
        return response.json()
    else:
        return None