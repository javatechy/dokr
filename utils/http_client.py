import requests 
# importing the requests library 
import json

# For GET requests
def get(URL, PARAMS):
    # sending get request and saving the response as response object 

    r = requests.get(url=URL, params=PARAMS) 
    # extracting data in json format 
    return r.json() 

# For POST requests
def post(URL, payload):
    # sending get request and saving the response as response object 
    print (URL)
    print (payload)
    headerss = {'content-type': 'application/json'}
    r = requests.post(url=URL, data=json.dumps(payload), headers=headerss)
    print("Status code is :" , r.status_code)
    print("Response text is :" + r.text)
    return r;