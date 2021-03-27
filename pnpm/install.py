from pathlib import Path
import site
from rich import print
import os
import subprocess as sp

def install():
    print("Installing pnpm...")
    PATH = site.getsitepackages()[0] + '/pnpm'

    # sp.call("pip install pnpm", shell=True)


    if 'zsh' in os.environ.get("SHELL", ""):
        print('Installing with zsh')
        with open(Path.home() / ".zshrc", 'a') as f:
            path = 'test'
            executable = f"python3 {PATH+'/generate.py'}"
            f.write("alias pnpm='() { " + executable + " echo $1  echo $2}'")
            

        #    alias example='(){ echo Your arg was $1. ;} 