import sys
import os
import utils.helper as utils
import utils.http_client as request
import json

def test_machine():
    usage  = utils.cmd_exec("docker exec -it fe0df5cdc63f  vmstat -s | grep 'memory'")
    url = "https://hooks.slack.com/services/XXX/XXX/XXXXXXX"
    data = {
        'text': '>>> This is `sent` \n from *dokr* plugin \n> Memory Left on your device : '+usage 
    }
    request.post(url,data)
    # test memory
    # Processor
    # Health testing in a machine
