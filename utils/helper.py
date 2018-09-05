import sys
import os


def cmd_exec(str):
    print("\n------------------------ Executing Command: Start ------------------------")
    print("\n$>>"+str);
    output = os.popen(str).read().strip();
    print("\n$>>" + output);
    print("\n------------------------ Executing Command: End ------------------------")
    return os.popen(str).read().strip()


def join_me(stringList):
    return "".join(string for string in stringList)

def helper():
    print('\n------------------------ Command Options ------------------------')
    print('\ndokr clean searchPattern # delete old images matching pattern')
    print('\ndokr clean-all searchPattern # clean docker')
    print('\ndokr lecs # ECS login')
    print('\ndokr tag searchPattern tagName # add a tag *tagName*on a image matching *searchPattern* ')
    print('\ndokr push searchPattern  # push all images matching the pattern')
    print('\n')