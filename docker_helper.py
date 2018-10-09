import sys
import os
import utils.helper as utils;

import utils.logger as logger;
import commons.config as config
import click


def add_build_tag(search_pattern, tag_name):
    logger.log_c("\nSearching pattern: " , search_pattern)
    logger.log_c("Adding tag : " + tag_name)
    image_name = utils.cmd_exec("docker images | cut -d ' '  -f1 | grep " + search_pattern + " | head -1");
    logger.log_y("Found this image name from the given pattern : " + image_name)
    add_tag_command = utils.join_me(['docker tag ' , image_name , ' ' , image_name , ':', tag_name ]);
    utils.cmd_exec(add_tag_command);
    logger.log_y('Added Tag : ' + tag_name + ' into the images\n')
    images_list = utils.cmd_exec('docker images')
    logger.log_c("Updated Images list :\n")
    logger.log(images_list)

  
def push_image(search_pattern):
    logger.log_c("\nSearching images matching this pattern : " + search_pattern)
    image_name = utils.cmd_exec("docker images | cut -d ' '  -f1 | grep " + search_pattern + " | head -1");
    logger.log_y("\nFound this image name from the given pattern : " + image_name)
    
    if image_name == '':
        logger.log_r("No such found to push !!! Exiting !!!")
        exit();
    image_list_str = "docker image inspect -f '{{join .RepoTags \"\\n\" }}' " + image_name;
    logger.debug("\nFinding images tags")
    image_list = utils.cmd_exec(image_list_str)
    logger.debug("\nFound Following images : \n\n" + image_list)
    tag_list = utils.cmd_exec(image_list_str).split("\n")
    logger.log_c('\nTotal Tags found : ' , str(len(tag_list)))
        
    for tag in tag_list:
        logger.log_c('\n--------------------------Pushing image :' + tag + '-----------------------------------')
        utils.cmd_exec('docker push ' + tag)


def clean_up(search_pattern):
    logger.log_c('\nCleaning Old Images  matching pattern : ' , search_pattern)
    logger.debug('\n----------  Cleaning Old Images ---- \n')
    utils.cmd_exec("docker images -a | grep " + search_pattern + " | awk '{print $3}' | xargs docker rmi -f")
    logger.log_g("\nCleaned images successfully")


def clean_all():
    logger.log_c('\nCleaning docker system')
    logger.log_y(utils.cmd_exec("docker system prune -a -f"))


def add_default_profile():
    registry = click.prompt(logger.style('\n[default] Your docker registry '), type=str)
    dir_mapping = click.prompt(logger.style('\n[default] Your default directory mapping '), type=str)
    env_vars = click.prompt(logger.style('\n[default] Environment vars(eg. ENV_NAME=dev)  '), type=str)
    config.set_env('default', 'docker_registry', registry)
    config.set_env('default', 'vol_mapping', dir_mapping)
    config.set_env('default', 'env_vars', env_vars)


def input_config_vars(profile_name, key_name, is_default_exist):
    if is_default_exist :
        default_value = config.get_env('default', key_name)
        user_input = click.prompt(logger.style('\nValue of ' + key_name), default=default_value, type=str)
    else:
        user_input = click.prompt(logger.style('\nYour ' + key_name), type=str)
    
    config.set_env(profile_name, key_name, user_input)
    

def add_profile(profile_name):
    config.add_profile(profile_name)
    config.set_env(profile_name, 'app_name', profile_name)
    input_config_vars(profile_name, 'docker_registry', True)
    input_config_vars(profile_name, 'vol_mapping', True)
    input_config_vars(profile_name, 'port_mapping', False)
    input_config_vars(profile_name, 'env_vars', True)

    
def run_profile(profile_name, tag_name):
    registry = config.get_env(profile_name, 'docker_registry')
    vol_mapping = config.get_env(profile_name, 'vol_mapping')
    port_mapping = config.get_env(profile_name, 'port_mapping')
    env_vars = config.get_env(profile_name, 'env_vars')
    
    command = "docker run -d "
    command += '--name ' + profile_name
    command += ' -p ' + port_mapping
    command += ' -v ' + vol_mapping
    command += ' -e ' + env_vars
    tag = 'latest'
    if tag_name == '':
        logger.log_bl('\nGetting top 5 available tags of ' + profile_name + ' from Amazon ECR registry...')
        tag_list = utils.cmd_exec("aws ecr describe-images --repository-name " + profile_name + " --output text --query 'sort_by(imageDetails,& imagePushedAt)[*].imageTags[*]' | tr '\t' '\n' | tail -5")
        tag_list = list(reversed(tag_list.split('\n')))
        tag = click.prompt(logger.style('\nSelect an tag to deploy: ?'), type=click.Choice(tag_list))
    logger.log_g('\nYou have selected tag: [ ' + tag + ' ]  for your application')
    command += ' ' + registry + '/' + profile_name + ':' + tag
    logger.debug('final command : ' + command)
    logger.log_y('\nKilling old container if exist')
    utils.cmd_exec('docker rm -f ' + profile_name)
    utils.cmd_exec(command)
    logger.log_g("\nSuccessfully started " + profile_name + " application . Please check logs using: ")
    logger.log_cy("\n                 docker logs -f " + profile_name + "                          \n")

    
def run_all():  
    profiles = config.get_profiles() 
    for profile in profiles :
        if profile == 'default' :
            continue
        logger.log_g("\n******************** Running Profile " + profile + " ********************")
        run_profile(profile, '')
