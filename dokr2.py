#!/usr/bin/env python
from __future__ import absolute_import

import utils.helper as utils;
import ecs_helper as ecs_helper;
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
@click.option('--ip', help='find Ip of a machine')
def aws(clean_all, clean, ip):
    if ip != None :
        ecs.find_ip()


@click.command()
@click.option('--clean', help='delete all images from your local docker matching the pattern')
@click.option('--clean-all' , help='Clean the whole docker system')
@click.option('--push', help='Push Image matching a pattern')
@click.option('--tag', type=(str, str), multiple=True, help='Add a tag given to an image')
def dock(clean, clean_all, push, tag):
    if clean != None :
         docker.clean_up(clean);
    if tag != None :
        for (key, value) in tag:
            docker.add_build_tag(key, value)
    if clean_all != None :
         docker.clean_all();
    if push != None :
        docker.push_image();


@click.command()
@click.argument('login', required=False)
@click.argument('deploy', required=False)
@click.argument('log', required=False)
@click.option('--cluster', required=False, help='Name of your cluster')
@click.option('--service', help='Name of your service')
@click.option('--tag', help='Tag of your image')
def ecs(login, deploy, log , cluster, service, tag):
    print (login)
    if login != None :
        print 'I am none'
        # ecs_helper.login_ecs()
    elif deploy != None: 
        if cluster == None:
            cluster = click.prompt('Give a cluster Name', type=str)
            service = click.prompt('Give a Service Name', type=str)
            tag = click.prompt('Give a Tag Name', type=str)
        ecs_helper.deploy();
    elif log != None:
	    ecs_helper.ecs_log()


dokecs.add_command(dock)
dokecs.add_command(ecs)
dokecs.add_command(aws)

if __name__ == '__main__':  # pragma: no cover
    dokecs()
