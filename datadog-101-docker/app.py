from datadog import initialize, statsd
from flask import Flask
from werkzeug.utils import url_quote
import os

# Initialize Datadog
ip = os.environ.get("DD_AGENT_HOST")
options = {
    'statsd_host': ip,
    'statsd_port': 8125
}
initialize(**options)

# Create a Flask app
app = Flask(__name__)

# Define a route
@app.route('/hello')
def hello():
    return "Hello from Flask!"