# Inventory Management System

## Overview

The Inventory Management System is a Flask application that allows the users to manage the food inventory. This system will allow employees to add, edit, view, and delete inventory items. Additionally, the system will fetch real-time product data from an external API (e.g., OpenFoodFacts API) to supplement product details.

## Features
1. View all products in the inventory
2. Add new products
3. Update any existing products
4. Delete existing products 
5. Search for products using an external API
6. Command-Line Interface(CLI)
7. Tests

## Technologies Used
1. Python 3
2. Flask
3. Request
4. Pytest
5. JSON

## Structure
Inventory management system
|
|-- app.py
|-- cli.py
|-- test
      |-- test_app.py
|-- README.md
venv/

## Installation

Clone the repository.
git clone <repository-url>

Navigate to the project folder.
cd "Inventory management system"

Create a virtual environment.
python3 -m venv venv

Activate the virtual environment.

Linux/macOS
source venv/bin/activate

Windows
venv\Scripts\activate

Install the required packages.
pip install -r requirements.txt

## Running the Application

Start the Flask server:
python app.py
Open another terminal, activate the virtual environment, and run the CLI:
python cli.py

## Example
{ "status": 1, 
"product_name": "Organic Almond Milk", 
"brands": "Silk", 
"ingredients_text": "Filtered water, almonds, cane sugar" }

## Running Tests

Run the automated test suite using:

pytest

Example output:

==================== test session starts ====================
collected 5 items

test_app.py .....                        [100%]

===================== 5 passed =====================

## Author 
Winfrey Wekesa

