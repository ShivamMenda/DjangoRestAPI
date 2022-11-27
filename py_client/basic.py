import requests
endpoint="http://localhost:8000/"
t=requests.get(endpoint)
print(t.text)
print(t.status_code)
