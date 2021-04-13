import subprocess as sb
import sys
import json
from script import config
# from config import config
import os

_params = json.loads(sys.argv[1]) if len(sys.argv)>1 else {}
def params(key=None):
    if key is None:
        return _params

    if key in _params:
        return _params[key]
    return None

print('yoing')
print(params())

env = params('env') or "dev"
pkg_manager = params('use') or config('package_manager')

if params("reload") or env=='prod':
    sb.call(f"pip3 install -r .pnpm/requirements.txt", shell=True)
    sb.call(f"{pkg_manager} install", shell=True)
# sb.call(f"source .docs_env/bin/activate", shell=True)



# def run(sub):
    # sp.call(f"python3 .pnpm/{sub}", shell=True)

def run(script):
    sb.call(f"python3 .pnpm/scripts/{script}", shell=True)

