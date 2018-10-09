# dokr - Make your docker and ecs tasks easy

A Helper pip package for docker and ECS tasks. This pip package helps you automate your CI/CD pipeline. If your using docker and Amazon ECS for deployments, this tool can be really helpful. This package uses aws cli and ecs cli. Mak


### Assumptions:

+ Assuming python is installed on your system.
+ Docker is installed on your system
+ [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)  is installed and credentials are configured on your system.
+ [ecs-cli](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html) is installed on system [*For Log Command only*]


Install `dokr` on your system using : 

```
pip install dokr
```

## ECS Options

+ login into ecs directly (Assuming awscli is installed and configured)

```
dokr ecs login
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_ecs_login.png)


+ Deploy an image on a cluster 

```
dokr ecs deploy --cluster cluster_name --service service_name --tag image_version
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_ecs_deploy.png)


+ Check ecs running logs of a Task -  this command will ask for cluster/service and task defination.

**Note:** Install ecs-cli before running this command  from here:
	  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html

```
dokr ecs log
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_ecs_log.png)


## Docker Helper Commands

+ Prune whole system -  Cleans unused images, containers and volumes.

```
dokr dock --clean-all
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_dock_clean_all.png)


+ Delete all the images matching the pattern

```
dokr dock --clean pattern_xxx
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_dock_clean.png)


+ Add a tag to the existing image matching the provided pattern  (for latest tag only)

```
dokr dock --tag pattern_xxx tag_name
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_dock_tag.png)



+ Push all images on a system matching a pattern

This will push all images matching pattern 'pat'

```
dokr dock --push pat
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_dock_push.png)


#### AWS Commands

+  Check current public ip of a machine on AWS

```
dokr aws --ip jenkins 
```

![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_aws_ip.png)


#### Run Apps (subsitute to `docker run` command and DockerCompose)

+ Configure your default values(like docker registry, port mapping, volume mapping etc. that will be same for all apps):

![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_configure.png)


+ Add an new app for deployment:

![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_configure_app.png)

+ Run all configured apps:

![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_run.png)

+ Run a particular  app from ECR tags:

![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_run_app.png)


+ Run a particular  app by providing a tag:

![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_run_app_tag.png)


### Development:

+ Clean ununsed: `rm -rf build/ dist/ *egg* **.pyc __pycache__`
+ Build package: `python setup.py bdist_wheel`
+ deploy package: `python -m twine upload dist/*`

follow this link for more details https://dzone.com/articles/executable-package-pip-install