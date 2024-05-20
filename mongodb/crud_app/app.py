from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB connection URI
uri = "mongodb://localhost:27017"
client = MongoClient(uri)

# Specify the database and collection
db = client.my_database
collection = db.my_collection

# Serve the HTML file
@app.route('/')
def serve_index():
    return render_template('index.html')

# Create (Insert) a new document
@app.route('/insert', methods=['POST'])
def insert_document():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        insert_result = collection.insert_one(data)
        return jsonify({"message": "Document inserted", "id": str(insert_result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Read (Get) all documents
@app.route('/documents', methods=['GET'])
def get_documents():
    try:
        documents = list(collection.find())
        for document in documents:
            document['_id'] = str(document['_id'])  # Convert ObjectId to string for JSON serialization
        return jsonify(documents), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Read (Get) a single document by ID
@app.route('/documents/<id>', methods=['GET'])
def get_document_by_id(id):
    try:
        document = collection.find_one({"_id": ObjectId(id)})
        if document:
            document['_id'] = str(document['_id'])  # Convert ObjectId to string for JSON serialization
            return jsonify(document), 200
        else:
            return jsonify({"error": "Document not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update a document by ID
@app.route('/documents/<id>', methods=['PUT'])
def update_document(id):
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        update_result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        if update_result.modified_count == 0:
            return jsonify({"message": "No document found to update"}), 404
        return jsonify({"message": "Document updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a document by ID
@app.route('/documents/<id>', methods=['DELETE'])
def delete_document(id):
    try:
        delete_result = collection.delete_one({"_id": ObjectId(id)})
        if delete_result.deleted_count == 0:
            return jsonify({"message": "No document found to delete"}), 404
        return jsonify({"message": "Document deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
