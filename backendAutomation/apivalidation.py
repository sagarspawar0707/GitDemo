import json

import requests

response=requests.get('http://216.10.245.166/Library/GetBook.php?',
             params={'ID':'bcd070519189'},)
#print(type(response.text))
#print(response.text)
#dict_response=json.loads(response.text)
#print(type(dict_response))
#print(dict_response[0]["isbn"])
json_response=response.json()
print(type(json_response))
print(json_response[0]["isbn"])
print(response.status_code)
assert response.status_code == 200
print(response.headers['Content-Type'])
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
print(response.cookies)