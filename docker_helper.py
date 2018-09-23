import sys
import os
import utils.helper as utils;


def add_build_tag():
    search_pattern = sys.argv[2];
    tag_name = sys.argv[3];
    print("\nSearching pattern: *" + search_pattern + "* and adding tag " + tag_name)
    image_name = utils.cmd_exec("docker images | cut -d ' '  -f1 | grep " + search_pattern + " | head -1");
    print("\nFound this image name from the given pattern : " + image_name)
    add_tag_command = utils.join_me(['docker tag ' , image_name , ' ' , image_name , ':', tag_name ]);
    utils.cmd_exec(add_tag_command);
    print('\nAdded Tag : ' + tag_name + ' into the images\n')
    utils.cmd_exec('docker images')

  
def push_image():
    search_pattern = sys.argv[2];
    print("\nPushing images matching pattern : " + search_pattern)
    image_name = utils.cmd_exec("docker images | cut -d ' '  -f1 | grep " + search_pattern + " | head -1");
    print("\nFound this image name from the given pattern : " + image_name)
    image_list_str = "docker image inspect -f '{{join .RepoTags \"\\n\" }}' " + image_name;
    print("\nFinding images tags")
    image_list = utils.cmd_exec(image_list_str)
    print("\nFound Following images : \n\n" + image_list)
    tag_list = utils.cmd_exec(image_list_str).split("\n")
    print('\nTotal Tags found :' , len(tag_list))
    for tag in tag_list:
        print('\n--------------------------Pushing image :' + tag + '-----------------------------------')
        print(utils.cmd_exec('docker push ' + tag))


def clean_up():
    search_pattern = sys.argv[2];
    print('\nCleaning Old Images  matching pattern ', search_pattern)
    print('\n----------  Cleaning Old Images ---- \n')
    utils.cmd_exec("docker images -a | grep " + search_pattern + " | awk '{print $3}' | xargs docker rmi -f")


def clean_all():
    print('\nCleaning docker system ')
    utils.cmd_exec("docker system prune -a -f")
    
