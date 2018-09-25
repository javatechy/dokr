# dokr

A Helper pip package for docker and ECS tasks

## ECS Options

#### login into ecs directly (Assuming awscli is installed and configured)

```
dokr ecs login
```

#### Deploy an image on a task

```
dokr ecs deploy --cluster cluster_name --service service_name --tag image_version
```


#### Check The options Available
```
dokr ecs login
```



#### Check ecs logs -  this command will ask for cluster/service and task defination.

- Install ecs-cli before running this command  from here:
	  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html

```
dokr ecs log
```



#### Prune docker system

```
dokr clean-all
```


#### Delete all the images matching the pattern

```
dokr clean pattern_xxx
```


#### Add a tag to the existing image matching the provided pattern  (for latest tag only)

```
dokr tag pattern_xxx tag_name
```


#### Push all images on a system matching a pattern

```
dokr push pattern_xxx
```



#### Check current public ip of a machine on AWS

```
dokr aws --ip jenkins 
```


### Development:

+ Clean ununsed: `rm -rf build/ dist/ *egg* **.pyc __pycache__`
+ Build package: `python setup.py bdist_wheel`
+ deploy package: `python -m twine upload dist/*`

follow this link for more details https://dzone.com/articles/executable-package-pip-install