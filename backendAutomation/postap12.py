import requests
import json
from payload import *
import configparser



addbook_response = requests.post(
    'http://216.10.245.166/Library/Addbook.php',
    json=addBookplayload("Sagar"),
    headers={"Content-Type": "application/json"})

json_response=addbook_response.json();
print(json_response)
bookid=json_response['ID']

#Delete book

response_delete=requests.post('http://216.10.245.166/Library/DeleteBook.php?',json={
        "ID": bookid
},headers={"Content-Type":"application/json"})
assert response_delete.status_code == 200
res_json=response_delete.json()
print(res_json['msg'])
assert res_json['msg'] == "book is successfully deleted"