import click
from .rmdir import rmdir
from .createproject import create_project

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

