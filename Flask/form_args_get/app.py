from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/form', methods=['GET'])
def get_data():
    user_input = request.args.get('data')
    if user_input:
        return f'You entered: {user_input.upper()}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
