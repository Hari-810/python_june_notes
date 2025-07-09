from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

@app.route('/api/posts', methods=['GET'])
def get_external_posts():
    try:
        r = requests.get(BASE_URL)
        r.raise_for_status()
        data = r.json()
        return jsonify({"status": "success", "data": data[:5]}), 200
    except requests.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/echo', methods=['POST'])
def post_echo():
    if not request.is_json:
        return jsonify({"status": "error", "message": "Invalid JSON"}), 400
    data = request.get_json()
    return jsonify({"status": "success", "received": data}), 200

@app.route('/api/post/<int:post_id>', methods=['GET'])
def get_single_post(post_id):
    try:
        r = requests.get(f"{BASE_URL}/{post_id}")
        r.raise_for_status()
        data = r.json()
        return jsonify({"status": "success", "data": data}), 200
    except requests.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/posts', methods=['POST'])
def create_post():
    if not request.is_json:
        return jsonify({"status": "error", "message": "Invalid JSON"}), 400
    payload = request.get_json()
    try:
        r = requests.post(BASE_URL, json=payload)
        r.raise_for_status()
        return jsonify({"status": "success", "data": r.json()}), 201
    except requests.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    if not request.is_json:
        return jsonify({"status": "error", "message": "Invalid JSON"}), 400
    payload = request.get_json()
    try:
        r = requests.put(f"{BASE_URL}/{post_id}", json=payload)
        r.raise_for_status()
        return jsonify({"status": "success", "data": r.json()}), 200
    except requests.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        r = requests.delete(f"{BASE_URL}/{post_id}")
        if r.status_code in [200, 204]:
            return jsonify({"status": "success", "message": f"Post {post_id} deleted"}), 200
        else:
            return jsonify({"status": "error", "message": "Failed to delete"}), 400
    except requests.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)




"""
### 🔌 **API Test Calls (cURL)**

**1. Get 5 Posts**

```bash
curl http://127.0.0.1:5000/api/posts
```

**2. Get Post by ID**

```bash
curl http://127.0.0.1:5000/api/post/1
```

**3. Create a Post**

```bash
curl -X POST http://127.0.0.1:5000/api/posts \
     -H "Content-Type: application/json" \
     -d '{"title": "New Title", "body": "Post body", "userId": 1}'
```

**4. Update a Post**

```bash
curl -X PUT http://127.0.0.1:5000/api/post/1 \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Title", "body": "Updated body", "userId": 1}'
```

**5. Delete a Post**

```bash
curl -X DELETE http://127.0.0.1:5000/api/post/1
```

**6. Echo JSON**

```bash
curl -X POST http://127.0.0.1:5000/api/echo \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, world!"}'
```

---

"""