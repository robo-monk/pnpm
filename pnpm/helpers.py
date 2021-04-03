import re
import subprocess as sb

regex = r"Location: ([^ ]+)"
_path = sb.check_output("pip3 show pnpm", shell=True).decode('utf-8').replace("\n", " ")
_path = re.search(regex, _path).group(1) + "/pnpm"

def abs_path(sub=''):
    return _path  + sub

