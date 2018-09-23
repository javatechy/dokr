#!/usr/bin/env python
from __future__ import absolute_import

import utils.helper as utils;
import ecs_helper as ecs;
import sys;
import docker_helper as docker;
import commons.config as config 
import click


@click.group()
@click.version_option(version=1.0, prog_name='dokr')
def dokecs():  # pragma: no cover
    pass


@click.command()
@click.argument('clean')
@click.argument('cleanall')
def docker(test):
    print test

    
@click.command()
@click.argument('clean')
@click.argument('deploy')
@click.argument('cleanall')
@click.argument('lecs')
def ecs(clean, deploy, cleanall, lecs):
    print ('clean' + clean)
    arg = 'hep'
    if clean :
        docker.clean_up();
    elif arg == 'deploy' :
        ecs.deploy();
    elif arg == 'clean-all':
        docker.clean_all();
    elif arg == 'lecs':
        ecs.login_ecs()
    elif arg == 'tag':
        docker.add_build_tag()
    elif arg == 'ip':
        ecs.find_ip()
    elif arg == 'push':  
        docker.push_image();
    elif arg == 'mcstatus':
	    mctest.test_machine()
    elif arg == 'log':
	    ecs.ecs_log() 
    elif arg == 'deploy':
	    ecs.deploy()
    elif arg == '--version':
	    config.find_version()
    else:
        utils.helper();


dokecs.add_command(docker)
dokecs.add_command(ecs)
       
if __name__ == '__main__':  # pragma: no cover
    dokecs()
