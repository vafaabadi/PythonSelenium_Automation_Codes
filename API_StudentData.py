import requests
import json
import jsonpath


# learning:   json.loads() ====== response.json()

def test_add_StudentData():
    #POST
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/Vafa/PycharmProjects/Auto_01/API_StudentData.json','r')
    json_request = json.loads(f.read())  # formating to JSON
    response = requests.post(API_URL,json_request)
    print(response.text)


def test_get_StudentData():
    # GET
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/61972"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)                                   # to format it to JSON format for assertion
    id = jsonpath.jsonpath(json_response, 'data.id')                            # to check id=3044. To "check" the input id=3044 is observed in output for asertion
    print(id)
    assert id[0] == 61972


def test_update_StudentData():
    # PUT
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/61972"
    f = open('C:/Users/Vafa/PycharmProjects/Auto_01/API_StudentData_Update.json', 'r')
    json_request = json.loads(f.read())  # formating to JSON
    response = requests.put(API_URL, json_request)                              # the difference between update and add is  put  in this line(and the file with different details).
    print(response.text)

    #ADDING GET RESPONSE AFTER UPDATE TO MAKE SURE THE UPDATE RESPONSE WORKED CORRECTLY AS FOLLOW(DUPLICATION OF GET RESPONSE TO FOR ASSERTION)
def test_get_StudentData():
    # GET
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/61972"
    response = requests.get(API_URL)
    json_response = response.json()
    print(json_response)                                                        #extra line: to see the message for comparison
    id = jsonpath.jsonpath(json_response,'data.id')
    print(id)
    assert id[0] == 61972                                               #I updated the DOB in the JSON file to 12/12/2000. so asserted here.

def test_delete_StudentData():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/61972"
    response = requests.delete(API_URL)
    print(response.text)


def test_get_StudentData():
    #ATTENTION: THIS LAST TEST CASE MUST FAIL BECAUSE THE PREVIOUS TEST CASE DELETE THE STUEDENT record. SO the CODE DOES NOT FETCH THE STUDENT UNDER THIS TEST CASE BECAUSE IT IS ALREADY DELETED.
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/61972"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    # print(id)
    assert id[0] == 61972
