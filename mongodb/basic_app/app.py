# pip install Flask pymongo
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection URI
uri = "mongodb://localhost:27017"
client = MongoClient(uri)

# Specify the database and collection
db = client.my_database
collection = db.my_collection

@app.route('/insert', methods=['POST'])
def insert_document():
    try:
        # Get JSON data from the request
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Insert the data into the collection
        insert_result = collection.insert_one(data)
        
        return jsonify({"message": "Document inserted", "id": str(insert_result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



#  Use Postman to Insert Data

# Open Postman.
# Create a new POST request to http://127.0.0.1:5000/insert.
# Set the request body to raw and select JSON format.
# Add the JSON data you want to insert. For example:
"""

{
    "name": "Jane Doe",
    "age": 32,
    "email": "jane.doe@example.com"
}

"""
# Send the request


