#!/usr/bin/env python
from __future__ import absolute_import

import utils.helper as utils;
import ecs_helper as ecs;
import sys;
import docker_helper as docker;
import commons.config as config 
import pkg_resources
import click

VERSION = pkg_resources.require("dokr")[0].version  
    

@click.group()
@click.version_option(version=VERSION, prog_name='dokr')
def dokecs():  # pragma: no cover
    pass


@click.command()
@click.option('--clean', help='Search Pattern')
@click.option('--clean-all', help='Search Pattern')
@click.option('--tag', help='Search Pattern')
def docker(clean, clean_all):
    if clean != None :
         docker.clean_up(clean);
    if clean_all != None :
         docker.clean_all(clean);
    if tag != None :
        docker.add_build_tag()
    if push != None :
        docker.push_image();
    

@click.command()
@click.option('--ip', help='find Ip of a machine')
def aws(ip):
    if clean != None :
        ecs.find_ip()


@click.command()
@click.option('--cluster', prompt='Cluster Name')
@click.option('--service', prompt='Service Name')
@click.option('--tag', prompt='Give your image tag')
def ecs(cluster, service, lecs):
    if clean :
        docker.clean_up();
    elif arg == 'deploy' :
        ecs.deploy();
    elif arg == 'clean-all':
        docker.clean_all();
    elif arg == 'lecs':
        ecs.login_ecs()
    elif arg == 'mcstatus':
	    mctest.test_machine()
    elif arg == 'log':
	    ecs.ecs_log() 
    elif arg == 'deploy':
	    ecs.deploy()
    else:
        utils.helper();


dokecs.add_command(dock)
dokecs.add_command(ecs)
dokecs.add_command(aws)

if __name__ == '__main__':  # pragma: no cover
    dokecs()
