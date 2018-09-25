# dokr

A Helper pip package for docker and ECS tasks

## ECS Options

#### login into ecs directly (Assuming awscli is installed and configured)

```
dokr ecs login
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_ecs_login.png)


#### Deploy an image on a task

```
dokr ecs deploy --cluster cluster_name --service service_name --tag image_version
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_ecs_deploy.png)


#### Check The options Available
```
dokr ecs login
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_ecs_login.png)



#### Check ecs logs -  this command will ask for cluster/service and task defination.

- Install ecs-cli before running this command  from here:
	  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html

```
dokr ecs log
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_aws_ip.png)



#### Prune docker system

```
dokr dock --clean-all
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_dock_clean_all.png)


#### Delete all the images matching the pattern

```
dokr dock --clean pattern_xxx
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_dock_clean.png)


#### Add a tag to the existing image matching the provided pattern  (for latest tag only)

```
dokr dock --tag pattern_xxx tag_name
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_dock_tag.png)

#### Add a tag to the existing image matching the provided pattern  (for latest tag only)

```
dokr ecs log
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_ecs_log.png)


#### Push all images on a system matching a pattern

```
dokr dock --push hello
```
![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_aws_ip.png)


#### Check current public ip of a machine on AWS

```
dokr aws --ip jenkins 
```

![alt dokr_aws_ip](https://raw.githubusercontent.com/javatechy/dokr/master/screenshots/dokr_aws_ip.png)



### Development:

+ Clean ununsed: `rm -rf build/ dist/ *egg* **.pyc __pycache__`
+ Build package: `python setup.py bdist_wheel`
+ deploy package: `python -m twine upload dist/*`

follow this link for more details https://dzone.com/articles/executable-package-pip-install