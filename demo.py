from pprint import pprint
import inquirer
import os
path = os.getcwd()

while True:
    dirs = [ name + '/' for name in os.listdir(path) if
            os.path.isdir(os.path.join(path, name))]
    dirs.insert(0, '.. (Move to Parent Directory)')
    dirs.insert(0, '. (Select this folder)')

    questions = [
        inquirer.List(
            "folder",
            message="Select the Folder: ",
            choices=dirs
        ),
    ]
    answers = inquirer.prompt(questions)
    print(os.path.join(path, answers['folder']))
    if answers['folder'].split(' ')[0] == '..':
        path = os.path.dirname(path)
    elif answers['folder'].split(' ')[0] == '.':
        path = os.path.dirname(path)
        break
    else:
        path = os.path.join(path, answers['folder'])

print(path)
