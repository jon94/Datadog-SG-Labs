import requests
import time

# Define your endpoint URLs
hello_url = "http://localhost:5000/hello"
simulate_error_url = "http://localhost:5000/simulate_error"

# Set the interval between requests in seconds
interval_seconds = 1

# Infinite loop to keep hitting the endpoints
while True:
    try:
        # Send a request to localhost:5000/hello
        response_hello = requests.get(hello_url)
        print(f"Response from {hello_url}: {response_hello.text}")

        # Send a request to localhost:5000/simulate_error
        response_error = requests.get(simulate_error_url)
        print(f"Response from {simulate_error_url}: {response_error.text}")

    except requests.RequestException as e:
        print(f"Error: {e}")

    # Wait for the specified interval before sending the next set of requests
    time.sleep(interval_seconds)