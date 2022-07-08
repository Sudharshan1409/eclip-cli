import click
import inquirer
import os
import json
import shutil

def create_project_folder(config_path, config_file_path):
    path = os.getcwd()
    print('path: ', path)
    if not os.path.exists(config_path):
        os.makedirs(config_path)
    while True:
        dirs = [ name + '/' for name in os.listdir(path) if
                os.path.isdir(os.path.join(path, name))]
        dirs.insert(0, '.. (Move to Parent Directory)')
        dirs.insert(0, '. (Select this folder)')

        questions = [
            inquirer.List(
                "folder",
                message="Select the default Projects Folder Path: ",
                choices=dirs
            ),
        ]
        answers = inquirer.prompt(questions)
        if answers['folder'].split(' ')[0] == '..':
            path = os.path.dirname(path)
        elif answers['folder'].split(' ')[0] == '.':
            break
        else:
            path = os.path.join(path, answers['folder'])
            
    with open(config_file_path, 'w') as f:
        f.write('{"projects_folder_path": "' + path + '"}')
    
    print('path: ', path)
    return path

def check_or_create_config():
    home_path = os.getenv('HOME')
    config_path = os.path.join(home_path, '.eclip')
    config_file_path = os.path.join(config_path, 'config.json')
    if os.path.exists(config_file_path):
        try:
            with open(config_file_path) as f:
                config_file = json.load(f)
                projects_folder_path = config_file['projects_folder_path']
        except:
            print('Error in reading config file')
            shutil.rmtree(config_path)
            print(config_path)
            projects_folder_path = create_project_folder(config_path, config_file_path)
    
        return projects_folder_path

    else:
        click.echo('No Config file found. Creating one at {}'.format(config_file_path))
        projects_folder_path = create_project_folder(config_path, config_file_path)
    
        return projects_folder_path

@click.command()
@click.argument("project_name", nargs=1, required=True)
def create_project(project_name):
    projects_folder_path = check_or_create_config()
    click.echo('projects_folder_path: {}'.format(projects_folder_path))

def create_python_project():
    pass

def create_nodejs_project():
    pass
