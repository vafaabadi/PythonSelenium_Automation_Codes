import json
import jsonpath
import requests



def test_API_Example():
    API_URL = "https://reqres.in/api/users?page=2"
    response = requests.get(API_URL)
    print(response.status_code)
    assert response.status_code == 200                   #validating response.status_code
    print(response.headers)
    print(response.headers.get('Date'))
    assert "2020" in response.headers.get('Date')
    print(response.headers.get('Server'))
    assert "cloudflare" in response.headers.get('Server')
    print(response.elapsed)

    json_response = json.loads(response.text)
    print(json_response)
    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(pages[0])
    assert pages[0] == 2
    #print("total pages: " + str(pages[0]))

    first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
    print(first_name[0])
    assert first_name[0] == "Michael"


    for i in range(0, 5):           #to fetch all the first names
        first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
        last_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].last_name')
        print(first_name[0]+last_name[0])

    for i in range(0, 5):
        email = jsonpath.jsonpath(json_response, 'data['+str(i)+'].email')
        print(email[0])


#def test_API_post():
#    API_URL="https://reqres.in/api/users"