#!/usr/bin/env python
from __future__ import absolute_import

import utils.logger as logger
import pkg_resources
import sys;

import click

import commons.config as config 
import docker_helper as docker;
import ecs_helper as ecs_helper;
import utils.helper as utils;

VERSION = pkg_resources.require("dokr")[0].version  

 
def debug_logging(verbose):
    if verbose == 1:
        click.echo(click.style("Debugging Level is set", fg='green'))
        logger.enable_debug()


@click.group()
@click.version_option(version=VERSION, prog_name='dokr')
def dokecs():  # pragma: no cover
    pass


@click.command()
@click.option('--ip', help='find Ip of a machine based on the given pattern')
@click.option('--v', count=True, help='Enable verbose logging')
def aws(ip, v):
    if ip != None :
        ecs_helper.find_ip(ip)


@click.command()
@click.option('--clean', help='delete all images from your local docker matching the pattern')
@click.option('--clean-all' , count=True, help='Clean the whole docker system')
@click.option('--push', help='Push Image matching a pattern')
@click.option('--tag', type=(str, str), multiple=True, help='Add a tag given to an image --tag <image_search_key> <tag_name>')
@click.option('--v', count=True, help='Enable verbose logging')
def dock(clean, clean_all, push, tag, v):
    debug_logging(v)
    if clean != None :
         docker.clean_up(clean);
    if tag != None :
        for (key, value) in tag:
            docker.add_build_tag(key, value)
    if clean_all == 1 :
         docker.clean_all();
    if push != None :
        docker.push_image(push);


@click.command()
@click.argument('login', required=False)
@click.argument('deploy', required=False)
@click.argument('log', required=False)
@click.option('--cluster', help='Name of your cluster')
@click.option('--service', help='Name of your service')
@click.option('--tag', help='Tag of your image')
@click.option('--v', count=True, help='Enable verbose logging')
def ecs(login, deploy, log , cluster, service, tag, v):
    debug_logging(v)  
    if login == 'login' :
        ecs_helper.login_ecs()
    if login == 'deploy' :
        if cluster == None:
            cluster = click.prompt('Give a cluster Name ', type=str)
        if service == None:
            service = click.prompt('Give a Service Name', type=str)
        if tag == None:
            tag = click.prompt('Give a Tag Name', type=str)
        ecs_helper.deploy(cluster, service, tag);
    if login == 'log' :
        ecs_helper.ecs_log()


@click.command()
@click.option('--app', help='Enable verbose logging')
@click.option('--v', count=True, help='Enable verbose logging')
def configure(app, v):
    debug_logging(v)
    if app != None :
        docker.add_profile(app)
    else: 
        docker.add_default_profile();


@click.command()
@click.option('--app', help='Give profile name to deploy [use dokr configure --app to create one] ')
@click.option('--tag', help='Give tag information')
@click.option('--v', count=True, help='Enable verbose logging')
def run(app, tag, v):
    debug_logging(v)
    if app != None and tag != None:
        docker.run_profile(app, tag)
    elif app != None:
        docker.run_profile(app, '')
    else: 
        docker.run_all();


dokecs.add_command(dock)
dokecs.add_command(ecs)
dokecs.add_command(aws)
dokecs.add_command(configure)
dokecs.add_command(run)

if __name__ == '__main__':  # pragma: no cover
    dokecs()
