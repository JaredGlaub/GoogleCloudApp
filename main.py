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
def predictionResults():
    bqclient = bigquery.Client()
    query_string = """SELECT * FROM ML.PREDICT (MODEL `census.census_model`,(SELECT * FROM `census.input_view` WHERE dataframe = 'prediction'))"""
    
    df = (
        bqclient.query(query_string)
        .result()
        .to_dataframe(
            # Optionally, explicitly request to use the BigQuery Storage API. As of
            # google-cloud-bigquery version 1.26.0 and above, the BigQuery Storage
            # API is used by default.
            create_bqstorage_client=True,
        )
    )
    shorten = df.head(10)
    json_results = shorten.to_json()
    return json_results

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
