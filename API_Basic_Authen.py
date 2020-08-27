import requests
from requests.auth import HTTPBasicAuth


def test_basic_authen():
    response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('vafaabadi12@gmail.com','TestAutomation01'))
    print(response.text)