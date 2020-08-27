import json
import jsonpath
import requests
import response


def test_add_new_student():
    global id
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/Vafa/PycharmProjects/Auto_01/request_chaining_add_student.json','r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(response.text)
    print(id[0])


def test_get_details():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    print(response.text)
