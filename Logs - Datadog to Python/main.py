import requests
import json

api_key = '<YOUR_API_KEY>'
app_key = '<YOUR_APP_KEY>'

query = 'service:second-service'

url = 'https://api.ap1.datadoghq.com/api/v1/logs-queries/list'

headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

data = {
    'query': query,
    'time': {
        'from': 'now - 1h',
        'to': 'now'
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)
# logs = response.json()['data'][0]['attributes']['data']
#
# for log in logs:
#     print(log['message'])
