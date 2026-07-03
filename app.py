#app.py
from flask import Flask, jsonify, request
from api import search_product
from inventory import inventory

app = Flask(__name__)

#home route
@app.route('/')
def home():
    return "<h1>Welcome to the Inventory Management System!</h1>"

#search route
@app.route('/search/<string:product_name>', methods=['GET'])
def search(product_name):
    result = search_product(product_name)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'message': 'Product not found.'}), 404

#get all products in the inventory
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify([inventory]), 200

#view each product in the inventory
@app.route('/inventory/<int:status>', methods=['GET'])
def view_inventory(status):
    product = next((item for item in inventory if item['status'] == status), None)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({'message': 'Product not found.'}), 404

#add new product to the inventory
@app.route('/inventory', methods=['POST'])
def add_product():
    data = request.get_json()
    new_status = max([item['status'] for item in inventory]) + 1 if inventory else 1
    new_product = {
        "status": new_status,
        "product_name": data['product_name'],
        "brands": data['brands'],
        "ingredients_text": data['ingredients_text']
    }
    inventory.append(new_product)
    return jsonify(new_product), 201

#update product in the inventory
@app.route('/inventory/<int:status>', methods=['PATCH'])
def update_product(status):
    data = request.get_json()
    product_to_update = next((item for item in inventory if item['status'] == status), None)
    if not product_to_update:
        return jsonify({'message': 'Product not found.'}), 404

    product_to_update['product_name'] = data.get('product_name', product_to_update['product_name'])
    product_to_update['brands'] = data.get('brands', product_to_update['brands'])
    product_to_update['ingredients_text'] = data.get('ingredients_text', product_to_update['ingredients_text'])
    return jsonify(product_to_update), 200

#delete product from the inventory
@app.route('/inventory/<int:status>', methods=['DELETE'])
def delete_product(status):
    product_to_delete = next((item for item in inventory if item['status'] == status), None)
    if not product_to_delete:
        return jsonify({'message': 'Product not found.'}), 404

    inventory.remove(product_to_delete)
    return jsonify({'message': 'Product deleted successfully.'})

if __name__ == '__main__':
    app.run(debug=True)