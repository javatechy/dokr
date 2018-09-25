import sys
import os
import utils.helper as utils;

import utils.logger as logger;


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
    
