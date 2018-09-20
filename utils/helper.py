import sys
import os
import subprocess
import shlex
import commons.constant as const


def cmd_exec(str):
    print("\n------------------------ Executing Command: Start ------------------------")
    print("\n$>>" + str);
    output = os.popen(str).read().strip();
    print("\n$>>" + output);
    print("\n------------------------ Executing Command: End ------------------------")
    return os.popen(str).read().strip()

def join_me(stringList):
    return "".join(string for string in stringList)


def running_cmd(cmd):
    print("Running command: \n")
    print(cmd)
    subprocess.call(cmd.split(" "))


def get_system_type():
    platform = sys.platform;
    system_name = "NA";
    if platform == "linux" or platform == "linux2":
       system_name = const.LINUX_OS
    elif platform == "darwin":
        system_name = const.MAC_OS
    elif platform == "win32":
        system_name = const.WINDOWS_OS
    return system_name;


def helper():
    print('\n------------------------ Command Options ------------------------')
    print('\ndokr clean searchPattern # delete old images matching pattern')
    print('\ndokr clean-all searchPattern # clean docker')
    print('\ndokr lecs # ECS login')
    print('\ndokr tag searchPattern tagName # add a tag *tagName*on a image matching *searchPattern* ')
    print('\ndokr push searchPattern  # push all images matching the pattern')
    print('\ndokr ip searchPattern  # push all images matching the pattern')
    print('\ndokr push searchPattern  # push all images matching the pattern')
    print("\ndokr ip searchPattern # Find Ip from your aws machine")
    print("\ndokr log # For cluster->service->task logging. Provided ecs-cli is installed")
    print('\n')