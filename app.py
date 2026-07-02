#app.py
from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

if __name__ == '__main__':
    app.run(debug=True)