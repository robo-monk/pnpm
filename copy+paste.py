import re
import subprocess as sb

regex = r"Location: ([^ ]+)"
_path = sb.check_output("pip3 show pnpm", shell=True).decode('utf-8').replace("\n", " ")
sb.call("pip3 uninstall pnpm -y", shell=True)
sb.call("pip3 install pnpm --upgrade", shell=True)
sb.call("python3 " + re.search(regex, _path).group(1) + "/pnpm/install", shell=True)

def abs_path(sub=''):
    return _path  + sub

