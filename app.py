#app.py
from flask import Flask, jsonify, make_response, request, redirect, url_for
from Inventory import Inventory, inventory

app = Flask(__name__)

#home route
@app.route('/')
def home():
    resp = make_response("<h1>Welcome to the Inventory Management System!</h1>")
    return resp

@app.route("/about")
def about():
    return "<h1>About the Inventory Management System</h1><p>This system allows you to manage your inventory efficiently.</p>"

if __name__ == '__main__':
    app.run(debug=True)