#!/usr/bin/env python

import fun_caller as fc
import ecs_helper as ecs;
import utils;
import sys;
import docker_helper as docker;

arg = sys.argv[1]

if arg == 'clean'  :
        docker.cleanUp();
elif arg == 'deploy' :
        ecs.deploy();
elif arg == 'clean-all':
        docker.cleanAll();
elif arg == 'lecs':
        ecs.loginEcs()
elif arg == 'tag':
        docker.addBuildTag()
elif arg == 'push':  
        docker.pushImage();
else:     
        utils.helper();