from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    # Get the 'name' query parameter from the URL
    name = request.args.get('name', 'Guest')
    
    # Display a simple message with the name parameter
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/?name=John

#--------------------------------------------------------

"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    # Get individual query parameters using request.args.get()
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'Unknown')
    city = request.args.get('city', 'Unknown')
    
    # Display the values of the query parameters
    return f'Hello, {name}! Age: {age}, City: {city}'

if __name__ == '__main__':
    app.run(debug=True)


# http://127.0.0.1:5000/?name=John&age=30&city=New+York
"""