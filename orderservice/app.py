from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

INVENTORY_SERVICE_URL = os.getenv('INVENTORY_SERVICE_URL', 'http://localhost:8080')

@app.route('/create-order', methods=['POST'])
def create_order():
    order_data = request.json
    items = order_data.get('items', [])

    for item in items:
        # Call Inventory Service to check stock
        response = requests.post(f"{INVENTORY_SERVICE_URL}/check-stock", json={"item": item})
        if response.status_code != 200 or not response.json().get('in_stock', False):
            return jsonify({"status": "failure", "message": f"Item {item} is out of stock"}), 400

    # If all items are in stock, proceed with the order
    return jsonify({"status": "success", "message": "Order created successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
