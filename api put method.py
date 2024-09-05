#from http.client import import responses
from turtledemo.forest import doit1

import requests
import json
import random
import string

#from Tools.scripts.generate_opcode_h import header
from urllib3 import request

#base url:
base_url="https://reqres.in/api"

#auth_token
auth_token="token ... token value"

def generate_random_email():
    domain="test.com"
    email_length=5
    random_string=''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email=random_string + "@" +domain
    return email

#put request
def put_request(user_id):
    url=base_url + f"/users/{user_id}"
    print("Put Url:" +url)
    headers={"Authorization":auth_token}
    data={
        "Name":"Reshma",
        "Email":generate_random_email(),
        "Phone Number":"9876543"
    }
    response=requests.put(url,json=data,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("Put method as:",json_str)
    #user_id=json_data["id"]
    #print("User id===========>",user_id)
    #print("...............post request is done.......................")
    #return user_id

#call
put_request(901)
