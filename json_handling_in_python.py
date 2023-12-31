# -*- coding: utf-8 -*-
"""JSON Handling in Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LSLHEaSGtwkKUlBlWcy9shZYXXeMwTzr
"""

import requests
import json

# Define the base URL
base_url = "http://host1.open.uom.lk:8080"

# Define the API endpoint for entering a new product
api_endpoint = "/api/products/"

# Define the JSON data for the new product
new_product_data = {
    "productName": "Araliya Basmathi Rice",
    "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
    "category": "Rice",
    "brand": "CIC",
    "expiredDate": "2023.05.04",
    "manufacturedDate": "2022.02.20",
    "batchNumber": 324567,
    "unitPrice": 1020,
    "quantity": 200,
    "createdDate": "2022.02.24"
}

# Convert the data to JSON format
json_data = json.dumps(new_product_data)

# Send a POST request to create the new product
response = requests.post(base_url + api_endpoint, data=json_data)

# Print the response code
print(response.status_code)

import requests

# Define the base URL
base_url = "http://host1.open.uom.lk:8080"

# Define the API endpoint for getting all products
api_endpoint = "/api/products/"

# Send a GET request to retrieve all products
response = requests.get(base_url + api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Check if the response contains a "data" key
    if "data" in data:
        products = data["data"]

        # Print the total number of products
        #total_products = len(products)
        #print("Total Number of Products:", total_products)

        # Print the details of each product
        print('{')
        print('"message":', '"SUCCESS"', ',')
        print('"data":[')
        for product in products:
            print("{")
            print('"id":', product["id"],",")
            print('"productName":', '"' ,product["productName"],'",')
            print('"description":', '"' ,product["description"],'",')
            print('"category":', '"' ,product["category"],'",')
            print('"brand":', '"' ,product["brand"],'",')
            print('"expiredDate":', '"' ,product["expiredDate"],'",')
            print('"manufacturedDate":','"' , product["manufacturedDate"],'",')
            print('"batchNumber":', product["batchNumber"],",")
            print('"unitPrice":', product["unitPrice"],",")
            print('"quantity":', product["quantity"],",")
            print('"createdDate":', '"' ,product["createdDate"],'"')
            print("},")
else:
    print(response.status_code)

print("]}")

