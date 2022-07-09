import click
from .rmdir import rmdir
from .createproject import create_project
from .utils import (create_project_folder, check_or_create_config, navigate)

@click.command()
def configure():
    projects_folder_path = check_or_create_config(force_configure=True)
    click.echo('projects_folder_path: {}'.format(projects_folder_path))

@click.group()
def cli():
    '''
        Eclip Command
    '''

    click.echo('''
    Eclip Command
    Enter "eclip help" for more information
            ''')
cli.add_command(rmdir)
cli.add_command(create_project)
cli.add_command(configure)

