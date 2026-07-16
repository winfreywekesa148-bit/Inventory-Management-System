import requests

inventory = [
    {
        "status": 1,
        "product_name": "Organic Almond Milk",
        "brands": "Silk",
        "ingredients_text": "Filtered water, almonds, cane sugar, ..."
            
    },
    {
        "status": 2,
        "product_name": "Gluten-Free Bread",
        "brands": "Udi's",
        "ingredients_text": "Water, brown rice flour, tapioca starch, ..."
    }
]

def search_inventory(product_name):
    url =  "https://world.openfoodfacts.org/cgi/search.pl"

    params={
            "search_terms": product_name,
            "search_simple": 1,
            "action": "process",
            "json": 1
        }
    
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None
    
    data = response.json()

    products = data.get("products", [])

    if not products:
        return None
    
    results = []

    for product in products[:10]:
        results.append({
        "status": "new_status",
        "product_name": data.get('product_name'),
        "brands": data.get('brands'),
        "ingredients_text": data.get('ingredients_text')
        })

    return results

