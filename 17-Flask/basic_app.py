from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  # Function to handle GET requests to the root path "/"
  return "Hello from Flask! This is a GET request."


@app.route("/firstpage")
def hello_world():
  # Function to handle GET requests to the root path "/"
  return "This is your first page"

if __name__ == "__main__":
  app.run(debug=True)



"""
We import the Flask class from the flask library.
We create an instance of the Flask class and name it app.
We use the @app.route("/") decorator to define a route for the root path (/).
The function hello_world() is associated with this route.
When a GET request is made to the root path, the hello_world() function is executed.
This function simply returns a string "Hello from Flask! This is a GET request."
"""