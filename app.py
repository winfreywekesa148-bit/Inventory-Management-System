#app.py
from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

# Inventory class to manage the inventory
class Inventory:
    def __init__(self, status, product_name, brands, ingredients_text):
        self.status = status
        self.product_name = product_name
        self.brands = brands
        self.ingredients_text = ingredients_text

    def to_dict(self):
        return {
            'status': self.status,
            'product_name': self.product_name,
            'brands': self.brands,
            'ingredients_text': self.ingredients_text
        }

inventory = [
    Inventory(
        1,
        "Organic Almond Milk",
        "Silk",
        "Filtered water, almonds, cane sugar, ..."
    )
]

#get all products in the inventory
@app.route('/inventory/<int:status>', methods=['GET'])
def get_inventory(status):
    filtered_inventory = next((item for item in inventory if item.status == status), None)
    return jsonify(filtered_inventory.to_dict()) if filtered_inventory else jsonify({'message': 'No products found for the given status.'}), 404

#add new product to the inventory
@app.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    new_status = max([item.status for item in inventory]) + 1 if inventory else 1
    new_product_name = data['product_name']
    new_brands = data['brands']
    new_ingredients_text = data['ingredients_text']

    new_product = Inventory(new_status, new_product_name, new_brands, new_ingredients_text)
    inventory.append(new_product)
    return jsonify(new_product.to_dict()), 201

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)