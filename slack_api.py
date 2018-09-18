import sys
import os
import utils.helper as utils
import utils.http_client as request
import json
import commons.config as config
import commons.constant as constant


def get_slack_url():
    if constant.SLACK_URI not in os.environ:
        uri = raw_input("What your slack URL ?")
        print ("Your URI is : " + uri)
        config.set_env(constant.SLACK_URI, "https://hooks.slack.com/services/" + uri)
    return config.get_env(constant.SLACK_URI);

def test_machine():
    url = get_slack_url();
    usage = utils.cmd_exec("docker exec -it fe0df5cdc63f  vmstat -s | grep 'memory'")
    message = raw_input("Enter the message you want to send : ")
    
    data = {
        'text': '>>> This is `sent` \n from *dokr* plugin \n>' + message + ' \n Memory Left on your device : ' + usage 
    }
    request.post(url, data)
