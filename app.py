from flask import Flask, request

# Flask is a micro web framework for Python
# It is used to build web applications quickly and easily
app = Flask(__name__)

# This is a list of stores with their items and prices
# It is used to store the data for the stores
stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

# This is a route that handles GET requests to the root URL
@app.route('/')
@app.get('/store')
# This is a route that handles GET requests to the /store URL
# It returns a JSON response with the list of stores
def get_stores():
    return {"stores": stores}

# This is a route that handles GET requests to the /store/<string:name> URL
@app.post('/store')
def create_store():
    # This function handles POST requests to create a new store
    # It gets the JSON data from the request and creates a new store
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return new_store, 201

# add store name to the url dynamically wherever client sends a request to the server
app.post("/store/<string:name>/item")
# This is a route that handles POST requests to the /store/<string:name>/item URL
# It creates a new item in the specified store
def create_store(name):
    # This function handles POST requests to create a new item in a store
    # It gets the JSON data from the request and creates a new item
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404