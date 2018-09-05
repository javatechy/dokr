import sys
import os
import utils.helper as utils
import json


def login_ecs():
    login = utils.cmd_exec("aws ecr get-login   | sed  's/-e none//g'")
    utils.cmd_exec(login)


def get_last_task_definations(family_prefix):
    task_definations = utils.cmd_exec("aws ecs list-task-definitions --family-prefix " + family_prefix);
    return json.loads(task_definations)['taskDefinitionArns'][-1]


def get_task_defination_json(task_def_name):
    task_defination_json = utils.cmd_exec("aws ecs describe-task-definition --task-definition " + task_def_name);
    return json.loads(task_defination_json)


def update_task_image_version(task_def_json, version_number):
    imageName = task_def_json['taskDefinition']['containerDefinitions'][0]['image'];
    imageName = imageName.split(':')[0] + ':' + version_number
    task_def_json['taskDefinition']['containerDefinitions'][0]['image'] = imageName;
    print (json.dumps(task_def_json, indent=4))
    return task_def_json;

def deploy():
    build_number = "10"
    region = "ap-south-1"
    service_name = "docker-ecs-boot-service"
    cluster = "ecs-cluster3"
    image_version = "v_" + build_number
    task_family = "docker_ecs_app_image"
    
    last_task_def_name = get_last_task_definations(task_family)
    task_def_json = get_task_defination_json(last_task_def_name)
    task_def_json = update_task_image_version(task_def_json, image_version)
    
    print ('Last Updated Task definations : ' + json.dumps(task_def_json, indent=4))
    
    # Create a new task definition for this build
    # aws ecs register-task-definition --family docker_ecs_app_image --cli-input-json file://docker_boot_app-v_8.json
    utils.cmd_exec("aws ecs register-task-definition --family " + task_family + " --cli-input-json " + json.dumps(task_def_json) )

    """
    
    # Update the service with the new task definition and desired count
    # aws ecs describe-task-definition --task-definition docker_ecs_app_image | egrep "revision" | tr "/" " " | awk '{print $2}' | sed 's/"$// | sed 's/,/ /g''
    REVISION = utils.cmd_exec("aws ecs describe-task-definition --task-definition $task_family | egrep 'revision' | tr '/' ' ' | awk '{print $2}' | sed 's/\"$//' | sed 's/,/ /g'")

    print ("current revision is $REVISION")

    # aws ecs describe-services --services docker-ecs-boot-service --cluster ecs-cluster3 --region ap-south-1

    print "Checking if a service for this task is created or not"

    SERVICES = utils.cmd_exec("aws ecs describe-services --services ${service_name} --cluster ${cluster} --region ${region} | jq .failures[]")

    print ("value of SERVICES " + SERVICES)

    # Create or update service

    if SERVICES == "":
        print "updating older service"
        # aws ecs describe-services --services docker-ecs-boot-service --cluster ecs-cluster3 --region ap-south-1 | jq .services[].desiredCount
        DESIRED_COUNT = utils.cmd_exec("aws ecs describe-services --services ${service_name} --cluster ${cluster} --region ${region} | jq .services[].desiredCount")
        if DESIRED_COUNT == "0":
            DESIRED_COUNT = "1"

        print "updating service definations"
        utils.cmd_exec("aws ecs update-service --cluster ${cluster} --region ${region} --service ${service_name} --task-definition ${task_family}:${REVISION} --desired-count ${DESIRED_COUNT} --deployment-configuration maximumPercent=100,minimumHealthyPercent=0")
    else :
        print("entered new service")
        utils.cmd_exec("aws ecs create-service --service-name ${service_name} --desired-count 1 --task-definition ${task_family} --cluster ${cluster} --region ${region}")
    """
