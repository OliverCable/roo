#!/usr/bin/env python3

import click
from subprocess import call


@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', '-n', default='', help='Provide a human friendly, project name for your wordpress container, defaults to the commit SHA.')
@click.option('--commit', '-c', default='master', help='Provide a Git commit Hash to pull a specific Wordpress version.')
@click.option('--port', '-p', default='8080', help='Provide a port to access sonarqube over.')

def build(name, commit, port):
    """
    Used to deploy a containerized wordpress app.\n
    Example:\n
      - To build: `roo-wp --name sherbertLemon --hash 5etr638u --port 24601`
      - To destroy: `roo-wp --name sherbertLemon` 
    """
    # If user didn't provide a name, use the hash for tagging.
    if not name:
        name = commit

    # Attempt to run Wordpress.
    run_image(name, commit, port)

def run_image(name, commit, port):
    # Prepare docker-compose command for call module.
    build_cmd = ''
    build_cmd += 'NAME=' + name + ' '
    build_cmd += 'HASH=' + commit + ' '
    build_cmd += 'PORT=' + port + ' '
    build_cmd += 'docker-compose '
    build_cmd += '--project-name ' + name + ' '
    build_cmd += 'up -d'
    click.echo(build_cmd)

    # Execute build command.
    try:
        call([build_cmd],shell=True)
    except:
        click.echo("Docker compose has failed: please check your inputs, " +
                   "or manually try the build to debug: `" + str(build_cmd) + "`")

@cli.command()
@click.option('--name', '-n', default='', help='Provide a human friendly, project name for your wordpress container, defaults to the commit SHA.')
@click.option('--commit', '-c', default='master', help='Provide a Git commit Hash to pull a specific Wordpress version.')

def destroy(name, commit):
    # If user didn't provide a name, use the hash for tagging.
    if not name:
        name = commit

    # Prepare destroy command.
    destroy_cmd = 'PORT=80 docker-compose '
    destroy_cmd += '-p ' + name + ' down'

    # Execute destroy command.
    try:
        call([destroy_cmd],shell=True)
    except:
        click.echo("Docker compose has failed: please check your inputs, " +
                   "or manually try the build to debug: `" + str(build_cmd) + "`")
