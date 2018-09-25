import click


all_colors = 'black', 'red', 'green', 'yellow', 'blue', 'magenta', \
             'cyan', 'white', 'bright_black', 'bright_red', \
             'bright_green', 'bright_yellow', 'bright_blue', \
             'bright_magenta', 'bright_cyan', 'bright_white'

# Colored logging
def log_c(str):  
    click.echo(click.style(str, fg='green'))


# Simple logging    
def log(str):  
    click.echo(click.style(str, fg='green'))


# blinking logging    
def log_b(str):  
    click.echo(click.style(str, blink=True))
