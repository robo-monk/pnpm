import subprocess as sb
import site
sb.call("pip3 install pnpm", shell=True)
sb.call("python3 " + site.getsitepackages()[0]+'/pnpm/install', shell=True)
