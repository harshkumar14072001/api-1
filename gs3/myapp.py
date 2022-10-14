# This is an type of application which will send request to the provided url to get data

import requests
import json
# this is the url to which we will send request

# # request is sending to the url
# r=requests.get(url=URL)
# # converting the data to json file and then storing it in data
# data = r.json()
# print(data)
URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data ={'id':id}
    json_data = json.dumps(data)
    r=requests.get(url = URL,data = json_data)
    data= r.json()
    print(data)

# get_data()

def post_data():
    data={
        'name':'Ravi',
        'roll':104,
        'city':'Dhanbad'
    }
    json_data=json.dumps(data)
    r=requests.post(url = URL,data = json_data)
    data= r.json()
    print(data)

# post_data()


def update_data():
    data={
        'id':2,
        'name':'Ravi',
        'roll':104,
        'city':'Dhanbad'
    }
    json_data=json.dumps(data)
    r=requests.put(url = URL,data = json_data)
    data= r.json()
    print(data)
