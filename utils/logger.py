import click
import logging

all_colors = 'black', 'red', 'green', 'yellow', 'blue', 'magenta', \
             'cyan', 'white', 'bright_black', 'bright_red', \
             'bright_green', 'bright_yellow', 'bright_blue', \
             'bright_magenta', 'bright_cyan', 'bright_white'


def log_c(*argv):
    if len(argv) == 1:
        click.echo(click.style(argv[0], fg='magenta'))
    if len(argv) == 2:
        click.secho(argv[0], nl=False)
        click.echo(click.style(argv[1], fg='green'))


def log_r(str2):  
    click.echo(click.style(str2, fg='red'))

def log_g(str2):  
    click.echo(click.style(str2, fg='green'))

def log_y(str2):  
    click.echo(click.style(str2, fg='yellow'))
    
    
def log_bl(str2):  
    click.echo(click.style(str2, fg='blue'))


# Colored logging
def debug(str):
    logging.debug(str)


# Colored logging
def debug_c(str):  
    logging.debug(str)


# Simple logging    
def log(str):  
    click.echo(click.style(str, fg='green'))


# blinking logging    
def log_b(str):  
    click.echo(click.style(str, blink=True))
