import click

debug_logging = False;

all_colors = 'black', 'red', 'green', 'yellow', 'blue', 'magenta', \
             'cyan', 'white', 'bright_black', 'bright_red', \
             'bright_green', 'bright_yellow', 'bright_blue', \
             'bright_magenta', 'bright_cyan', 'bright_white'


def log_c(*argv):
    if len(argv) == 1:
        click.echo(click.style(argv[0], fg='magenta', bold=True))
    if len(argv) == 2:
        click.secho(argv[0], nl=False)
        click.echo(click.style(argv[1], fg='green', bold=True))


def log_r(str2):  
    click.echo(click.style(str2, fg='red', bold=True))


def style(str):
    return click.style(str, fg='cyan', bold=True)


def log_cy(str):
    click.echo(click.style(str, fg='cyan', bold=True))

def log_cyb(str):
    click.echo(click.style(str, fg='cyan', bold=True, blink=True))


def log_g(str2):  
    click.echo(click.style(str2, fg='green', bold=True))


def log_y(str2):  
    click.echo(click.style(str2, fg='yellow', bold=True))
    
    
def log_bl(str2):  
    click.echo(click.style(str2, fg='blue', bold=True))


# Colored logging
def debug(str):
    if debug_logging :
        click.secho((str))


# Colored logging
def debug_c(str): 
    if debug_logging: 
        click.echo(click.style(str, fg='blue', bold=True))


# Colored logging
def enable_debug(): 
    global debug_logging 
    debug_logging = True


# Simple logging    
def log(str):  
    click.echo(click.style(str, fg='green', bold=True))


# blinking logging    
def log_b(str):  
    click.echo(click.style(str, blink=True))
