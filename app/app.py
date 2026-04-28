from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter('app_requests_total', 'Total requests', ['endpoint'])

@app.route("/")
def home():
    REQUESTS.labels(endpoint="/").inc()
    return "Hello World"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

app.run(host="0.0.0.0", port=8000)