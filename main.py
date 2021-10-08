from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/name/<name>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/helloWorld')
def helloWorld():
    val = {"value": "hello World"}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)