#CLI Interface
from urllib import response
from inventory import inventory
import requests

#view items
def view_inventory():
    response = requests.get("http://127.0.0.1:5000/inventory")
    if response.status_code == 200:
        inventory = response.json()
        
        if not inventory:
            print("No products in the inventory.")
        else:
            print("Inventory:")
            for item in inventory:
                print(item)
                print(type(item))

#add new items
def add_product():
    requests.post("http://127.0.0.1:5000/inventory", json={
        "product_name": input("Enter product name: "),
        "brands": input("Enter brands: "),
        "ingredients_text": input("Enter ingredients text: ")
    })

    print("Product added successfully.")

#update items
def update_product():
    status = int(input("Enter the status of the product to update: "))

    response = requests.get(f"http://127.0.0.1:5000/inventory/{status}")

    if response.status_code != 200:
        print("Product not found.")
    else:
        product = response.json()
        print(f"Current product details: {product}")

        new_product_name = input(f"Enter new product name (current: {product['product_name']}): ")
        new_brands = input(f"Enter new brands (current: {product['brands']}): ")
        new_ingredients_text = input(f"Enter new ingredients text (current: {product['ingredients_text']}): ")

        response = requests.patch(f"http://127.0.0.1:5000/inventory/{status}", json={
            "product_name": new_product_name,
            "brands": new_brands,
            "ingredients_text": new_ingredients_text
        })
    print("Product updated successfully.")


#delete items
def delete_product():
    status = int(input("Enter the status of the product to delete: "))
    requests.delete(f"http://127.0.0.1:5000/inventory/{status}")
    print("Product deleted successfully.")

#search items
def search_inventory():
    product_name = input("Enter product name: ")

    response = requests.get(f"http://127.0.0.1:5000/search/{product_name}")

    if response.status_code == 200:

        products = response.json()

        print("\nProducts Found\n")

        for product in products:
            print("Product Name :", product["product_name"])
            print("Brand        :", product["brands"])
            print("Ingredients  :", product["ingredients"])

    elif response.status_code == 404:
        print("Product not found.")

    
def display_menu():
    menu = """
===== Inventory Management System =====
1. View Inventory
2. Add Product
3. Update Product
4. Delete Product
5. Search Product
6. Exit
"""
    while True:
        print(menu)
        choice = input("Enter your choice: ")

        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_product()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            search_inventory()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    display_menu()
