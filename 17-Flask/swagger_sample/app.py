# from flask import Flask
# from flask_restful import Api, Resource
# from flasgger import Swagger

# app = Flask(__name__)
# api = Api(app)
# swagger = Swagger(app)


# class HelloWorld(Resource):
#     def get(self):
#         """
#         This is the example endpoint.
#         """
#         return {'message': 'Hello, World!'}


# api.add_resource(HelloWorld, '/')


# if __name__ == '__main__':
#     app.run(debug=True)

#----------------------------------------------------------------------------

from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/add', methods=['POST'])
def add_numbers():
    """
    Add two numbers.

    ---
    parameters:
      - name: num1
        in: formData
        type: number
        required: true
        description: The first number.
      - name: num2
        in: formData
        type: number
        required: true
        description: The second number.
    responses:
      200:
        description: The sum of the two numbers.
    """
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')

    try:
        result = float(num1) + float(num2)
        return {'result': result}, 200
    except ValueError:
        return {'message': 'Invalid input. Please provide valid numbers.'}, 400


if __name__ == '__main__':
    app.run(debug=True)

# ------------------------------------------------------------------------



# http://127.0.0.1:5000/apidocs/