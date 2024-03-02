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

# Define a Hello World route
@app.route('/hello')
def hello():
    return "Hello from Flask!"

# Define error simulation endpoint
@app.route('/simulate_error')
def simulate_error():
    try:
        # Simulate an error by dividing by zero
        result = 1 / 0
    except Exception as e:
        # Return a JSON response with the error message
        return jsonify({'error': str(e)}), 500