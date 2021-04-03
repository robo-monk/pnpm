from pathlib import Path
from rich import print
import os
import subprocess as sp
from pnpm import helpers as hp

# helpers
def _params(length=3):
    return " ".join([f"${i}" for i in range(1, length+1)])

def alias(name, executable, _params_length):
    return "alias " + name + "='() { " + executable + " " + _params(_params_length) + "}'"

def install():
    print("Installing pnpm...")
    PATH = hp.abs_path()

    if 'zsh' in os.environ.get("SHELL", ""):
        print('Installing with zsh')
        with open(Path.home() / ".zshrc", 'r') as f:
            if "alias pnpm" in f.read():
                return print('pnpm is already installed!')
            
        with open(Path.home() / ".zshrc", 'a') as f:
            path = 'test'
            executable = f"python3 {hp.abs_path('/cli')}"
            f.write(alias('pnpm', executable, 5))
            