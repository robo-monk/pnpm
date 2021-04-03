import subprocess as sb
import site
sb.call("pip install pnpm", shell=True)
sb.call("python3 " + site.getsitepackages()[0]+'/pnpm/install', shell=True)
