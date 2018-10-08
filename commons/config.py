import json 
import os 
import pkg_resources
import sys
import click

import configparser 

import utils.logger as logger

config = configparser.SafeConfigParser()


def get_config_path():
    homedir = os.environ.get('HOME', None)
    logger.debug("Home Directory: " + homedir)
    if not homedir:
        logger.log_r("Home Directory Not found!! Set Envirnoment `HOME` ")
        exit()
    logger.debug("Home Directory : " + homedir)
    config_file = os.path.join(homedir + "/.dokr/config")
    logger.debug("Config File Location : " + config_file)
    if not os.path.exists(config_file):
        logger.log_r("ERROR: No Config file present")
        try:
            os.makedirs(os.path.dirname(config_file))
        except OSError as exc:  # Guard against race condition
            logger.log_r("Directory found! but not config file")
            
        logger.debug("Creating config file")
        file = open(config_file, "w") 
        file.write("[default]") 
        file.close() 
        
    logger.debug(config.read(config_file))
    return config_file;


config_file = get_config_path();

 
def ask_for_new_profile():
    add_profile('deepak')
    print(get_env('fabhotelier', 'ecr_repository'))
    print(set_env('fabhotelier', 'ecr_repository', 'My'))
    print(set_env('deepak', 'ecr_repository', 'My'))


def set_env(profile, key , value):
     config.set(profile, key, value)
     write_config()


def add_profile(profile):
    if config.has_section(profile):
        logger.log_r(profile + " Section already exists!!")
        return
    
    config.add_section(profile)
    write_config()


def write_config():
    with open(config_file, 'w') as configfile:
        config.write(configfile)


def get_env(profile, key):
    logger.debug("Searching in profile : " + profile)
    logger.debug("Searching in key" + key)
    if config.has_option(profile, key):
        return config.get(profile, key)
    logger.debug("Not found in current profile")
    if config.has_option('default', key):
        return config.get('default', key)
    
    logger.debug("No Value Found in DEAFULT SECTION as well")
    logger.log_r('Value not found in [Default Profile] use `dokr configure`comamnd')
    exit()

    
def get_profiles():
    return config.sections()


def log_config():
    level_input = 'DEBUG';
    if level_input == 'DEBUG':
        print(level_input)
        logging.basicConfig(level=logging.DEBUG)


def find_version():
    version = pkg_resources.require("dokr")[0].version  
    print (version)      

