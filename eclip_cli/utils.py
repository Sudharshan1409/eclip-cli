import os
import shutil
import json
import inquirer

def navigate(path):
    while True:
        dirs = [ name + '/' for name in os.listdir(path) if
                os.path.isdir(os.path.join(path, name))]
        dirs.insert(0, '.. (Move to Parent Directory)')
        dirs.insert(0, '. (Select this folder)')

        questions = [
            inquirer.List(
                "folder",
                message="Navigate to the folder where you want to create the project: ",
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
    return path


def create_project_folder(config_path, config_file_path):
    path = os.getcwd()
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

def check_or_create_config(force_configure=False):
    home_path = os.getenv('HOME')
    config_path = os.path.join(home_path, '.eclip')
    config_file_path = os.path.join(config_path, 'config.json')
    if force_configure and os.path.exists(config_file_path):
        shutil.rmtree(config_path)
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
        print('No Config file found. Creating one at {}'.format(config_file_path))
        projects_folder_path = create_project_folder(config_path, config_file_path)
    
        return projects_folder_path



