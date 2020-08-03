'''
file: os_basics.py
description: 
    python script exploring the various 
    features and use cases of python os module
'''

import os

# print cwd
print(f'CWD : {os.getcwd()} \n')

print(f'Doing an ls : \n \t {os.listdir()} \n')

# list files in each directory
def list_files(startpath):
    for root,dirs,files in os.walk(startpath):
        if dir!='.git':
            level = root.replace(startpath,'').count(os.sep)
            indent = '' *4 * (level)
            print(f'{indent}{os.path.basename(root)}/')
            subindent = '' *4 * (level+1)
            for f in files:
                print(f'{subindent}{f}')

startpath = os.getcwd()
list_files(startpath)


