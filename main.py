from flask import Flask
from flask import jsonify
from google.cloud import bigquery

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

@app.route('/prediction')
    client = bigquery.Client()

    SELECT  FROM `burnished-ember-328422.census.predictionResults` LIMIT 10

    df = client.query(sql).to_dataframe()
    json_results = df.to_json()
    return json_results

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)