#import the necessary model
import requests
import json
#base url
base_url="https://reqres.in/api"

#authorization token
auth_token="token token value"

def get_request():
    url=base_url + "/users/"
    print("Get url:" +url)    #+concradination string
    headers={"Authorization":auth_token}
    response=requests.get(url, headers=headers)
    assert response.status_code==200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("Json get requet Body",json_str)
    print("get user is done")
    print("*****")

get_request()
