from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock inventory data
inventory = {
    "item1": 10,
    "item2": 5,
    "item3": 0  # Out of stock
}

@app.route('/check-stock', methods=['POST'])
def check_stock():
    item_data = request.json
    item = item_data.get('item')

    in_stock = inventory.get(item, 0) > 0
    return jsonify({"item": item, "in_stock": in_stock})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
