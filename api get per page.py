from http.client import responses

import requests
import json
#base url
base_url="https://reqres.in/api"

#authorization token
auth_token="token token value"

def get_request(page):
    url=f"{base_url}/user?page={page}"
    print(f"Get url:{url}")
    headers={"Authorization ":auth_token} if auth_token else {}
    response =requests.get(url,headers=headers)
    assert response.status_code==200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print(f"Json Get response Body for page {page}:",json_str)
    print("Get user is done")
    print("******")

get_request(3)