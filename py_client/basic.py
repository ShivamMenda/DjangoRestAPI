import requests
endpoint="http://localhost:8000/api/"
t=requests.post(endpoint,json={"title":"hello","price":"120","content":"test"})
#print(t.text)
#print(t.status_code)
print(t.json())
