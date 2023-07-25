from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods = ['GET'])  # api endpoint
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET']) 
def result():
   if request.method == 'POST':
      form_result = request.form
      return render_template("result.html",result = form_result)

if __name__ == '__main__':
   app.run(debug = True)  