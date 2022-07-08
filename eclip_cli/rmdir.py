import click
import os
import shutil
@click.command()
@click.argument("directory", nargs=-1, required=True)
@click.argument("path", nargs=1, required=True)
def rmdir(directory, path):
    print(directory, path)
    if os.path.exists(path):
        print(os.path.abspath(path))
        for root, dirs, files in os.walk("."):
            if root.split('/')[-1] == 'node_modules' or root.split('/')[-1] == 'venv':
                print('removing', root)
                shutil.rmtree(root)
    else:
        click.echo("Path does not exist")
        exit()
   


