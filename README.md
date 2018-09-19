# dokr

A Helper pip package for docker and ECS tasks


#### Check The options Available

```
dokr help
```

#### login into ecs directly (Assuming awscli is installed and configured)

```
dokr lecs
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


###Development:

+ Clean ununsed: `rm -rf build/ dist/ *egg* **.pyc __pycache__`
+ Build package: `python setup.py bdist_wheel`
+ deploy package: `python -m twine upload dist/*`

follow this link for more details https://dzone.com/articles/executable-package-pip-install