import requests
import json
import jsonpath
import time

#the note pad used for this test case is in the same folder under the name of API_Test_e2e.txt


def test_Add_new_data():
    #Adding student
    App_URL="http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/Vafa/PycharmProjects/Auto_01/API_Test_e2e.json','r')
    request_json = json.loads(f.read())
    response = requests.post(App_URL,request_json)
    id = jsonpath.jsonpath(response.json(),'id')                        #fetch IDs from the response
    print(id[0])

    #Adding technical details
    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    f = open('C:/Users/Vafa/PycharmProjects/Auto_01/API_Test_e2e_technicalskills.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    time.sleep(2)
    #Adding address
    add_api_url = "http://thetestingworldapi.com/api/addresses"
    f = open('C:/Users/Vafa/PycharmProjects/Auto_01/API_Test_e2e_addresses.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(add_api_url, request_json)
    #print(response.text)

    time.sleep(2)
    #Fetching complete details
    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/3044"
    response = requests.get(final_details)
    print(response.text)