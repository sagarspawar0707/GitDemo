
import requests
import json
from payload import *
import configparser
from utilites.configurations import *
from utilites.recource import *
"""
url=getconfig()['API']['endpoint']+ApiResources.addBook
addbook_response = requests.post(url,
    json=addBookplayload("Sagar"),
    headers={"Content-Type": "application/json"})

json_response=addbook_response.json();
print(json_response)
bookid=json_response['ID']

#Delete book
url1=getconfig()['API']['endpoint']+ApiResources.deleteBook
response_delete=requests.post(url1,json={
        "ID": bookid
},headers={"Content-Type":"application/json"})
assert response_delete.status_code == 200
res_json=response_delete.json()
print(res_json['msg'])
assert res_json['msg'] == "book is successfully deleted"
"""
#authentication
se=requests.session();
se.auth=('sagarspawar0707',getpassword())
url2='https://github.com/sagarspawar0707'
github_response=se.get(url2)

print(github_response.status_code)

url3='https://github.com/sagarspawar0707'
response1=requests.get(url3,auth=('sagarspawar0707',getpassword()))
print(response1.status_code)


