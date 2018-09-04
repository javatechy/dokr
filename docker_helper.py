#!/usr/bin/env python

import sys
import os
import utils


def addBuildTag():
    searchPattern = sys.argv[2];
    tagName = sys.argv[3];
    print('\nSearching pattern: *', searchPattern + '* and adding tag ' + tagName)
    imageName = utils.cmdExec("docker images | cut -d ' '  -f1 | grep " + searchPattern + " | head -1");
    print('\nFound this image name from the given pattern ' , imageName)
    addTagCommand = utils.joinMe(['docker tag ' , imageName , ' ' , imageName , ':', tagName ]);
    print('\nExecuting tag command : \n' + addTagCommand)
    print(utils.cmdExec(addTagCommand));
    print('\nAdded Tag : ' + tagName + ' into the images\n')
    print(utils.cmdExec('docker images'))

  
def pushImage():
    searchPattern = sys.argv[2];
    print('\nPushing images matching pattern ', searchPattern)
    
    imageName = utils.cmdExec("docker images | cut -d ' '  -f1 | grep " + searchPattern + " | head -1");
    
    print('\nFound this image name from the given pattern ' , imageName)
    
    imageListStr = "docker image inspect -f '{{join .RepoTags \"\\n\" }}' " + imageName;
    imageList = utils.cmdExec(imageListStr)
    
    print('\nFound Following images : \n\n' + imageList)
    
    tagList = utils.cmdExec(imageListStr).split("\n")
    
    print('\nTotal Tags found :' , len(tagList))
    
    for tag in tagList:
        print('\n--------------------------Pushing image :' + tag + '-----------------------------------')
        print(utils.cmdExec('docker push ' + tag))

def cleanUp():
    searchPattern = sys.argv[2];
    print('\nCleaning Old Images  matching pattern ', searchPattern)
    print('\n----------  Cleaning Old Images ---- \n')
    cleaner = utils.cmdExec("docker images -a | grep " + searchPattern + " | awk '{print $3}' | xargs docker rmi -f")
    print(cleaner)


def cleanAll():
    print('\nCleaning docker system ')
    cleaner = utils.cmdExec("docker system prune -a -f")
    print(cleaner)
