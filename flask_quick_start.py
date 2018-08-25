#!/usr/bin/env python3
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
parser.add_argument('-g', '--git', action='store_true')
args = parser.parse_args()

"""
Global variables
"""
script_dir = os.path.dirname(os.path.realpath(__file__))

"""
Colors for terminal output
"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# copy flask structure into new directory 
def create_project(appname, project_path, structure):
    project = os.path.join(project_path, appname)
    struct = os.path.join(script_dir, structure)
    shutil.copytree(struct, project)

# vertualenv creation as venv into project directory 
def init_virtualenv(project_path, appname):
    project = os.path.join(project_path, appname)
    # initialize vitualenv for project
    output, error = subprocess.Popen(
        [
            'virtualenv',
            os.path.join(project, 'venv')
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE).communicate()
    if error:
        print(bcolors.FAIL + f'An error occured: \n{error}' + bcolors.ENDC,
              end="")
        sys.exit(2)

    venv_bin = os.path.join(project, 'venv/bin')
    # install requirements 
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
        print(bcolors.FAIL +
            f'An error occured during requiremets installation: \n{error}' +
            bcolors.ENDC, end="")
        sys.exit(2)

# git init
def init_git(project_path, appname):
    project = os.path.join(project_path, appname)
    # initialize git in project dir
    output, error = subprocess.Popen(
        [
            'git',
            'init',
            project
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE).communicate()
    if error:
        print(bcolors.FAIL +
              f'An error occured during git init: \n{error}' +
              bcolors.ENDC, end="")
        sys.exit(2)
    # copy over .gitinore
    shutil.copyfile(
        os.path.join(script_dir, '.gitinore'),
        os.path.join(project, '.gitinore')
    )

if __name__ == "__main__":
    create_project(args.appname[0], args.path[0], args.structure[0])
    print(bcolors.OKGREEN +
          f'{args.appname[0]}: Created successfully!!' + bcolors.ENDC, end="")
    if args.virtualenv:
        init_virtualenv(args.path[0], args.appname[0])
        print(bcolors.OKGREEN +
          '\nVirtualenv created successfully!!' + bcolors.ENDC, end="")
    if args.git:
        init_git(args.path[0], args.appname[0])
        print(bcolors.OKGREEN +
          '\nGit successfully initialized!!' + bcolors.ENDC, end="")

