# -*- coding: utf-8 -*-

import argparse
import shutil
import os
import sys
import subprocess

"""
Parser Args
"""
parser = argparse.ArgumentParser(description='Flask-Quick-Start. A simple\
                                 commandline application for setting up a\
                                 simple flask project structure.')
parser.add_argument('appname', metavar='A', type=str, nargs=1, help='The app\
                    name.')
parser.add_argument('-p', '--path', type=str, nargs=1, default=[os.getcwd()],
                    help='The path of new project.')
parser.add_argument('-s', '--structure', type=str, nargs=1, help='Structure to use.')
parser.add_argument('-v', '--virtualenv', action='store_true')
args = parser.parse_args()

"""
Global variables
"""
script_dir = os.path.dirname(os.path.realpath(__file__))

# copy flask structure into new directory 
def create_project(appname, project_path, structure):
    project = os.path.join(project_path, appname)
    struct = os.path.join(script_dir, structure)
    shutil.copytree(struct, project)

# vertualenv creation as venv into project directory 
def init_virtualenv(project_path, appname):
    project = os.path.join(project_path, appname)
    output, error = subprocess.Popen(
        [
            'virtualenv',
            os.path.join(project, 'venv')
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE).communicate()
    if error:
        print(f'An error occured:\n {error}')
        sys.exit(2)
    venv_bin = os.path.join(project, 'venv/bin')
    output, error = subprocess.Popen(
        [
            os.path.join(venv_bin, 'pip'),
            'install',
            '-r',
            os.path.join(project, 'requirements.txt')
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE).communicate()
    if error:
        print(f'An error occured during requiremets installation: \n{error}')
        sys.exit(2)

# git init
def init_git():
    pass 

if __name__ == "__main__":
    create_project(args.appname[0], args.path[0], args.structure[0])
    init_virtualenv(args.path[0], args.appname[0])
