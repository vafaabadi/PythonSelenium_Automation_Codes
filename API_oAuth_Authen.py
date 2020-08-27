import json
import jsonpath
import requests
import response
from requests.auth import HTTPBasicAuth


def test_oauth_authen():
    token_url="http://thetestingworldapi.com/Token"
    data={'grant_type':'password','username':'admin','password':'adminpass'}
    response = requests.post(token_url,data)
    print(response.text)
    token_value=jsonpath.jsonpath(response.json(),'access_token')

    auth={'Authorization':'Bearer '+token_value[0]}
    API_URL = 'http://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(API_URL, headers=auth)
    #response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('vafaabadi12@gmail.com','TestAutomation01'))
    print(response.text)