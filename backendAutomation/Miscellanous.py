import requests

#'visit-month'
se=requests.session()
se.cookies.update({'visit-month':'November'})
cookie={'visit-month':'November'}

reponse=requests.get("https://rahulshettyacademy.com/",allow_redirects=False,cookies=cookie,timeout=1)
#print(reponse.history)
print(reponse.status_code)

#response2=requests.get('https://httpbin.org/cookies',cookies=cookie)
response2=se.get('https://httpbin.org/cookies')
cooke_response=response2.json();
print(response2.history)
print(response2.text)
print(cooke_response)