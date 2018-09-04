#!/usr/bin/env python

import sys
import os
import utils

def loginEcs():
    login = utils.cmdExec("aws ecr get-login   | sed  's/-e none//g'")
    print('\n----------  Logining into aws  ----------  \n\n', login + '\n')
    print(utils.cmdExec(login))

def deploy():
    print ('deploying on ecs cluster')

