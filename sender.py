import requests

headers = {
    'Content-type': 'application/json',
}

json_data = {
    'text': 'hello!',
}

response = requests.post(
    f'https://hooks.slack.com/services/T0838QEFVPY/B083FFZD96E/{os.environ.get("SLACK_ID")}',
    headers=headers,
    json=json_data,
)

print(response)
