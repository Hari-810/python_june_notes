from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods = ['GET'])  # api endpoint
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST']) 
def result():
   if request.method == 'POST':
      form_result = request.form
      numerical_values = [int(value) for key, value in form_result.items() if value.isdigit()]
      avg_result = sum(numerical_values)//len(numerical_values)
      return render_template("result.html",result = form_result,avg_result = avg_result)

if __name__ == '__main__':
   app.run(debug = True)  