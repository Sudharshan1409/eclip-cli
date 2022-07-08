import os
import shutil

for root, dirs, files in os.walk("."):
    if root.split('/')[-1] == 'node_modules' or root.split('/')[-1] == 'venv':
        print('removing', root)
        shutil.rmtree(root)
