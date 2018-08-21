import argparse, os, sys, shutil

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
def verlualenv():
    pass

# git init
def init_git():
    pass 

if __name__ == "__main__":
    create_project(args.appname[0], args.path[0], args.structure[0])
