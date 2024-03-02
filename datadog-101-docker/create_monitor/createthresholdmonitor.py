import requests
import json

api_key = 'YOUR_API_KEY'
app_key = 'YOUR_APP_KEY'

headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key,
}

monitor_payload = {
    "name": "Service flask-dd-lab has a high error rate on env:dd-sg-lab",
    "type": "query alert",
    "query": "sum(last_10m):( sum:trace.flask.request.errors{env:dd-sg-lab,service:flask-dd-lab}.as_count() / sum:trace.flask.request.hits{env:dd-sg-lab,service:flask-dd-lab}.as_count() ) > 0.05",
    "message": "`flask-dd-lab` error rate is too high.",
    "tags": [
        "service:flask-dd-lab",
        "env:dd-sg-lab"
    ],
    "options": {
        "thresholds": {
            "critical": 0.05
        },
        "notify_audit": False,
        "threshold_windows": {},
        "include_tags": False
    }
}

url = 'https://api.datadoghq.com/api/v1/monitor'
response = requests.post(url, headers=headers, data=json.dumps(monitor_payload))

if response.status_code == 200:
    print("Monitor created successfully!")
else:
    print(f"Failed to create monitor. Status code: {response.status_code}, Response: {response.text}")