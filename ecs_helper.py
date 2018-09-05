import sys
import os
import utils.helper as utils;

def login_ecs():
    login = utils.cmdExec("aws ecr get-login   | sed  's/-e none//g'")
    utils.cmdExec(login)

def deploy():
    print ('deploying on ecs cluster')
    """
    BUILD_NUMBER="10"
    REGION="ap-south-1"
    SERVICE_NAME="docker-ecs-boot-service"
    CLUSTER="ecs-cluster3"
    IMAGE_VERSION="v_" + BUILD_NUMBER
    TASK_FAMILY="docker_ecs_app_image"
    # Create a new task definition for this build
    # sed -e "s;%BUILD_NUMBER%;${BUILD_NUMBER};g" ./docker_boot.json > docker_boot_app-v_8.json
    utils.cmdExec("sed -e 's;%BUILD_NUMBER%;"+BUILD_NUMBER+ ";g ./docker_boot.json > docker_boot_app-v_"+BUILD_NUMBER+".json") 
    
    # aws ecs register-task-definition --family docker_ecs_app_image --cli-input-json file://docker_boot_app-v_8.json
    aws ecs register-task-definition --family $TASK_FAMILY --cli-input-json file://docker_boot_app-v_${BUILD_NUMBER}.json

    # Update the service with the new task definition and desired count
    # aws ecs describe-task-definition --task-definition docker_ecs_app_image | egrep "revision" | tr "/" " " | awk '{print $2}' | sed 's/"$// | sed 's/,/ /g''
    REVISION=`aws ecs describe-task-definition --task-definition $TASK_FAMILY | egrep "revision" | tr "/" " " | awk '{print $2}' | sed 's/"$//' | sed 's/,/ /g'`

    echo "current revision is $REVISION"

    # aws ecs describe-services --services docker-ecs-boot-service --cluster ecs-cluster3 --region ap-south-1

    print "Checking if a service for this task is created or not"

    SERVICES=`aws ecs describe-services --services ${SERVICE_NAME} --cluster ${CLUSTER} --region ${REGION} | jq .failures[]`

    echo "value of SERVICES  : $SERVICES"

    #Create or update service

    if SERVICES == "":
        print "updating older service"
        # aws ecs describe-services --services docker-ecs-boot-service --cluster ecs-cluster3 --region ap-south-1 | jq .services[].desiredCount
        DESIRED_COUNT=`aws ecs describe-services --services ${SERVICE_NAME} --cluster ${CLUSTER} --region ${REGION} | jq .services[].desiredCount`
        if [ ${DESIRED_COUNT} = "0" ]; then
        DESIRED_COUNT="1"

        echo "updating service definations"
        aws ecs update-service --cluster ${CLUSTER} --region ${REGION} --service ${SERVICE_NAME} --task-definition ${TASK_FAMILY}:${REVISION} --desired-count ${DESIRED_COUNT} --deployment-configuration maximumPercent=100,minimumHealthyPercent=0
    else
        echo "entered new service"
        aws ecs create-service --service-name ${SERVICE_NAME} --desired-count 1 --task-definition ${TASK_FAMILY} --cluster ${CLUSTER} --region ${REGION}

    """
