from flask import Flask
from flask_restful import Api, Resource
from flask_restful_swagger import swagger

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='1.0')


class HelloWorld(Resource):
    @swagger.operation(
        notes='Get a friendly greeting',
        responseClass=dict,
        nickname='hello'
    )
    def get(self):
        """
        Get a friendly greeting
        """
        return {'message': 'Hello, World!'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)
