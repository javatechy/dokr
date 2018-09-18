import logging

SLACK_URI = 'DOKR_SLACK_URI'

LOGGING_LEVEL = {
    'DEBUG' : logging.DEBUG,
    'INFO' : logging.INFO
    }
# # ECS CLI  contants

MAC_OS = 'mac'
LINUX_OS = 'linux'

ECS_CLI_INSTRUCTIONS = """ [MAC]:\n 
        sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest\n 
        chmod +x /usr/local/bin/ecs-cli
        
        -------   for LINUX ---------\n
        sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest \n 
        chmod +x /usr/local/bin/ecs-cli
        
        further steps:
        follow readme.md
        https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html
        """

ECS_CLI_PATH_MAP = {
    'mac' : '/usr/local/bin/ecs-cli',
    'linux' : '/usr/bin/ecs-cli'
    }
