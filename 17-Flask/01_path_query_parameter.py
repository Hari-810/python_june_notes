from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Return a simple 'Hello, World!' message.
    """
    return "Hello, World!"

@app.route('/sum')
def sum_numbers():
    """
    Get query parameters 'a' and 'b' and return their sum.
    
    Returns:
        JSON object: {"result": sum}
            sum (int): The sum of parameters 'a' and 'b'.
            
        If either 'a' or 'b' is missing, returns a JSON object with an error message.
    """
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        return jsonify(error="Parameters 'a' and 'b' are required.")
    return jsonify(a + b)

@app.route('/multiply/<int:a>/<int:b>')
def multiply_numbers(a, b):
    """
    Get path parameters 'a' and 'b' and return their product.
    
    Parameters:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        JSON object: {"result": product}
            product (int): The product of parameters 'a' and 'b'.
    """
    return jsonify(result=a * b)

if __name__ == '__main__':
    app.run(debug=True)


"""
http://127.0.0.1:5000/                   will return "Hello, World!"
http://127.0.0.1:5000/sum?a=3&b=5        will return {"result": 8}
http://127.0.0.1:5000/multiply/4/6       will return {"result": 24}

"""



#----------------------------------------------------------------------------------



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