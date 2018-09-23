import os 
import json 
import sys
import logging
import pkg_resources  # part of setuptools


def set_env(key , value):
    pass


def get_env(key):
    return ''


def log_config():
    level_input = 'DEBUG';
    if level_input == 'DEBUG':
        print(level_input)
        logging.basicConfig(level=logging.DEBUG)

        
def find_version():
    version = pkg_resources.require("dokr")[0].version  
    print (version)      
