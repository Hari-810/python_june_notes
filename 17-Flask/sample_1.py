from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return '<h1>Hello World<h1>'

@app.route('/score/<int:score>/<int:score_2>')    #int score 
def hello_name(score,score_2):
   return ("the score you entered: {} {}".format(score,score_2))
@app.route('/world')
def world():
   return "<h1>World<h1>"

if __name__ == '__main__':
   app.run(debug=True)




