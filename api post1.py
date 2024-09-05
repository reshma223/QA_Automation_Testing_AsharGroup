#from http.client import import responses

import requests
import json

#from Tools.scripts.generate_opcode_h import header

#base url:
base_url="https://reqres.in/api"

#auth_token
auth_token="token ... token value"

#post request
def post_request():
    url=base_url + "/users/"
    print("PostUrl:" +url)
    headers={"Authorization":auth_token}
    data={
        "Name":"Reshma",
        "Email":"reshma@gmail.com",
        "Job":"QALearner"
    }
    response=requests.post(url,json=data,headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("Json Post response body:",json_str)
    user_id=json_data["id"]
    print("User id===========>",user_id)
    assert response.status_code==201
    print("...............post request is done.......................")
    return user_id

user_id=post_request()
