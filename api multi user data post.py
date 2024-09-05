from http.client import responses
import requests
import json

#base url:
base_url=("https://reqres.in/api")
#auth_token:
auth_token="token ...token value"

#Post the multi users
def post_request(user_names):
    url=base_url + "/users/"
    print("Post url:" + url)
    headers={"Authorization": auth_token}
    user_ids=[]

    for name in user_names:
        data={
            "name":name,
            "Job":"QA learner"
        }

        response =requests.post(url,json=data,headers=headers)
        json_data=response.json()
        json_str=json.dumps(json_data,indent=4)
        print("Post response body for",name, ":", json_str)
        user_id=json_data.get("id")
        if user_id:
            user_ids.append(user_id)
        assert response.status_code==201

        assert "name" in json_data
        print("........==========post user is created successfully for",name,"...........")
    return user_ids

#user name example
user_names=["Prem","Binita","Aayuska","Reshma"]
#user_ids=post_request(user_names)
for _ in range(10):
    user_ids=post_request(user_names)
print("Created user_Ids:",user_ids)

















