import requests
import json

# Set your Datadog API key and application key
DATADOG_API_KEY = 'YOUR_API_KEY'
DATADOG_APP_KEY = 'YOUR_APP_KEY'

# Datadog API endpoint for getting a list of hosts
DATADOG_HOSTS_API_URL = 'https://api.datadoghq.com/api/v1/hosts'

def check_host_exists(host_name):
    headers = {
        'Content-Type': 'application/json',
        'DD-API-KEY': DATADOG_API_KEY,
        'DD-APPLICATION-KEY': DATADOG_APP_KEY
    }

    # Query parameters for searching hosts by name
    params = {'filter': 'host:{}'.format(host_name)}

    try:
        response = requests.get(DATADOG_HOSTS_API_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
        hosts_data = response.json()

        if hosts_data['total_matching'] > 0:
            print(f"Host '{host_name}' exists in Datadog.")
        else:
            print(f"Host '{host_name}' does not exist in Datadog.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_host_name' with the actual host name you want to check
    host_to_check = 'your_host_name'
    check_host_exists(host_to_check)
