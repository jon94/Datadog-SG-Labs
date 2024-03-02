import requests
import json

api_key = 'YOUR_API_KEY'
app_key = 'YOUR_APP_KEY'

headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

monitor_payload = {
    "name": "[APM Trace Analytics Monitor] simulation_error service",
    "type": "trace-analytics alert",
    "query": "trace-analytics(\"service:simulate_error resource_name:simulate_error env:dd-sg-lab status:error\").rollup(\"count\").last(\"5m\") > 20",
    "message": "Alert! High Error on resource {{span.resource_name}} in env {{span.env}} ,
    "tags": [
        "service:simulate_error",
        "env:dd-sg-lab"
    ],
    "options": {
        "thresholds": {
            "critical": 20
        },
        "enable_logs_sample": False,
        "notify_audit": False,
        "on_missing_data": "default",
        "include_tags": False
    }
}

url = 'https://api.datadoghq.com/api/v1/monitor'
response = requests.post(url, headers=headers, data=json.dumps(monitor_payload))

if response.status_code == 200:
    print("Monitor simulate_error created successfully!")
else:
    print(f"Failed to create monitor. Status code: {response.status_code}, Response: {response.text}")