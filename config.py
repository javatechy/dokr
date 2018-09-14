import os 

def set_env(key , value):
    os.environ[key] = value;


def get_env(key):
    return os.environ[key]