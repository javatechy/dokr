import os 
import json 
import sys
import logging

pth = os.getcwd() + "/commons/config.json";

    
def read_config():
    logging.info("pth" + pth)
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
    data[key] = value
    write_config(data)


def get_env(key):
    return read_config()[key]


def log_config():
   # level_input = sys.argv[2];
    level_input = 'DEBUG';
    if level_input == 'DEBUG':
        print level_input
        logging.basicConfig(level=logging.DEBUG)
