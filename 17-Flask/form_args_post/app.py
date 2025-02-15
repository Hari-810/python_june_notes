from flask import Flask, request, render_template

app = Flask(__name__)

# Route to display the form
@app.route('/')
def display_form():
    return render_template('form.html')

# Route to process the form data
@app.route('/process', methods=['POST'])
def process_form():
    # Retrieve form data using request.form
    name = request.form.get('name')
    email = request.form.get('email')

    # You can now use 'name' and 'email' in your application logic
    return f"Received form data. Name: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=True)
"""

---

### **When to Use Each?**
| Scenario | Use |
|----------|-----|
| Retrieving **URL parameters** (e.g., `/search?q=flask`) | `request.args.get()` |
| Retrieving **form data** submitted via `POST` | `request.form.get()` |
| If unsure whether the data comes from **query parameters or form data** | `request.values.get()` (checks both) |

"""