from rich import console as _console, print, inspect
console = _console.Console()

from .config import config
from .script import * 


import json
import os
import sys

def warn(*args, **kwargs):
    console.print(" × ", *args, "🔫 ", **kwargs, style="#FF851B bold")