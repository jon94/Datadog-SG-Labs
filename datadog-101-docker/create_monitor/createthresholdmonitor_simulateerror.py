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
	"name": "Service simulate_error has a high error rate on env:dd-sg-la",
	"type": "query alert",
	"query": "sum(last_10m):(sum:trace.app.simulate_error.errors{env:dd-sg-lab, service:simulate_error}.as_count() / sum:trace.app.simulate_error.hits{env:dd-sg-lab, service:simulate_error}.as_count()) > 0.05",
	"message": "`simulate_error` error rate is too high.",
	"tags": [],
	"options": {
		"thresholds": {
			"critical": 0.05
		},
		"notify_audit": false,
		"include_tags": false,
		"notify_no_data": false,
		"silenced": {}
	},
	"priority": null,
	"restricted_roles": null
}
url = 'https://api.datadoghq.com/api/v1/monitor'
response = requests.post(url, headers=headers, data=json.dumps(monitor_payload))

if response.status_code == 200:
    print("Monitor simulate_error created successfully!")
else:
    print(f"Failed to create monitor. Status code: {response.status_code}, Response: {response.text}")