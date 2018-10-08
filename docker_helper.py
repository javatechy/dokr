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
    registry = click.prompt('[default] Your docker registry :', type=str)
    dir_mapping = click.prompt('[default] Your default directory mapping :', type=str)
    docker_env = click.prompt('[default] Environment Name eg. ENV_NAME  :', type=str)
    config.set_env('default', 'docker_registry', registry)
    config.set_env('default', 'vol_mapping', dir_mapping)
    config.set_env('default', 'docker_env', docker_env)


def add_profile(profile_name):
    config.add_profile(profile_name)
    
    config.set_env(profile_name, 'app_name', profile_name)
    registry = config.get_env('default', 'docker_registry')
    dir_mapping = click.prompt('Your registry :', default=registry, type=str)
    config.set_env(profile_name, 'docker_registry', registry)    
    
    vol_mapping = config.get_env('default', 'vol_mapping')
    vol_mapping = click.prompt('Your volume mapping :', default=vol_mapping, type=str)
    config.set_env(profile_name, 'vol_mapping', vol_mapping)
    
    port_mapping = click.prompt('Port Mapping :', type=str)
    config.set_env(profile_name, 'port_mapping', port_mapping)
    
    repository_name = click.prompt('Repository Name :', default=profile_name, type=str)
    config.set_env(profile_name, 'repo_name', repository_name)
    
    env_vars = config.get_env('default', 'env_vars')
    env_vars = click.prompt('Repository Name :', env_vars, type=str)
    config.set_env(profile_name, 'env_vars', env_vars)

    
def run_profile(profile_name):
    
    registry = config.get_env('default', 'docker_registry')
    vol_mapping = config.get_env(profile_name, 'vol_mapping')
    port_mapping = config.get_env(profile_name, 'port_mapping')
    repo_name = config.get_env(profile_name, 'repo_name')
    env_vars = config.get_env(profile_name, 'env_vars')
    
    command = "docker run -d "
    command += '--name ' + profile_name
    command += ' -p ' + port_mapping
    command += ' -v ' + vol_mapping
    command += ' -e ' + env_vars
    
    tag_list = utils.cmd_exec("aws ecr describe-images --repository-name " + repo_name + " --output text --query 'sort_by(imageDetails,& imagePushedAt)[*].imageTags[*]' | tr '\t' '\n' | tail -10")
    tag_list = list(reversed(tag_list.split('\n')))
    logger.log_r('Select an image tag to deploy')
    logger.log_y('\n'.join(tag_list)) 
    tag = click.prompt('Select an tag to deploy: ?', type=click.Choice(tag_list))
    logger.log_c('selected tag ' , tag)
    command += ' ' + registry + ':' + tag
    
    print('final command : ' + command)


def run_all():  
    profiles = config.get_profiles() 
    for profile in profiles :
        if profile == 'default' :
            continue
        
        print ("Profile name  " + profile)
        run_profile(profile)
