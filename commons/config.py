import os 
import json 
import sys

pth = os.getcwd() + "/commons/config.json";

    
def read_config():
    with open(pth) as json_file:  
        data = json.load(json_file)
    return data


def write_config(data):
    with open(pth, 'w') as outfile: 
        json.dump(data, outfile, indent=4)


def enable_debugging():
    data = read_config()
    data['debug'] = True
    write_config(data)


def set_env(key , value):
    data = read_config()
    write_config(data)


def get_env(key):
    data = read_config()
    return data['key']

