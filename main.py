from flask import Flask, jsonify, request, render_template
from google.cloud import bigquery

app = Flask(__name__, template_folder='./userinterface/build')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def index():
    return render_template("index.html")

# @app.route('/')
# def name():
#     val = "Hello World"
#     return jsonify(val)

@app.route('/name/<name>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/login',  methods=['GET', 'POST'])
def login():
    deviceid = request.values.get('deviceid')
    return '/login - device: {}\n'.format(deviceid)

@app.route('/metrics',  methods=['GET', 'POST'])
def metrics():
    deviceid = request.values.get('deviceid')
    timestamp = request.values.get('timestamp')
    
    return '/metrics - device: {}, timestamp: {}\n'.format(deviceid, timestamp)

@app.route('/prediction')
def predictionResults():
    bqclient = bigquery.Client()
    query_string = """SELECT predicted_income_bracket,probability, top_feature_attributions FROM `burnished-ember-328422.census.predictionResults` LIMIT 10"""
    
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
    shorten = df.head(2)
    json_results = shorten.to_json()
    return json_results

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
