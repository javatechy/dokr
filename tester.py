#!/usr/bin/env python

import fun_caller as fc
import ecs_helper as ecs;
import utils;
import sys;
import docker_helper as docker;

arg = sys.argv[1]

if arg == 'clean'  :
    docker.clean_up();
elif arg == 'deploy' :
    ecs.deploy();
elif arg == 'clean-all':
    docker.clean_all();
elif arg == 'lecs':
    ecs.login_ecs()
elif arg == 'tag':
    docker.add_build_tag()
elif arg == 'push':  
    docker.push_image();
else:     
    utils.helper();