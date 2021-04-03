from rich import print
from pnpm import install as i

__version__ = '0.2.1'

def whoisthis():
    print(f"This is {__version__}")

def _install():
    i.install()
    