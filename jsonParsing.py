import json
"""
courses = '{"name":"SagarPawar","languages":["Java","Python"]}'

#loads method parse json string and it returns dictionary

dict_courses=json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print((dict_courses['name']))
# Accessing the list of languages
list_of_languages = dict_courses['languages'][0]
print(list_of_languages)

# Accessing the first element of the list
#print(list_of_languages[0])
#first_language = list_of_languages[0]
#print(first_language)
for key in dict_courses.keys():
    print(key)

for values in dict_courses.values():
    print(values)

for key ,values in dict_courses.items():
    print(key,'::' ,values)

"""

#*****Parse content present in Json file

with open("D:\\json\\Demo3.json",'r') as file:
       data_dic=json.load(file)
       print(data_dic)
       print(type(data_dic))
       print(data_dic['courses'][1]['title'])
       print(data_dic['dashboard'])
       print(data_dic['dashboard']['website'])
# get price of RPA course
       print(data_dic['courses'][2]['price'])

#price of course 'RPA'
       data_dic['courses']

       for course in data_dic['courses']:
           #print(course)
           if course['title']=='RPA':
               print(course['price'])
               assert course['price'] == 45

with open("D:\\json\\Demo4.json", 'r') as file1:
    data_dic1 = json.load(file1)
    assert data_dic == data_dic1
