# pnpm - Pragmatic Node PNPM Manager

## Requirements:
- Python 3
- Node.js
- npm/yarn/yarn2

## Install with `cURL` and `pip` 

### `zsh`
```
curl -sSL raw.githubusercontent.com/robo-monk/pnpm/master/copy%2Bpaste.py | python3 - && zsh
```
> other shells are supported but I haven't implemented the installation script for them yet

## Generate new package

```bash
pnpm create 
```
> and add information via the prompts


## Commands

```bash
pnpm dev      # will start server and will watch files for changes
pnpm build    # will bundle the application (--env production to build for production)

pnpm release  # will bunlde the application in production, ask for a new version, 
              # run tests if configed so and publish to npm repository. You can pass --patch
              # --prepatch (pnpm release --prepatch), it will automatically bump the version
              # and will not ask for confirmation
        
# any other command of npm or yarn
pnpm add pragmajs # == yarn add pragmajs if you use yarn (if you use npm it will break)
pnpm install pragmajs --save-dev # == npm i pragmajs --save-dev
```

## Extending
You can ofcourse add your own python script to extend the pnpm's functionality for the project that you're currently working on. You should try not to hard-code names, like the package name for example and use the `params()` or `config()`. Here's an example:
```python
#!/usr/local/bin/python3

from script import *           # imports a banch of useful libraries like os, sys,
                               # json and more, functions like warn, spawn, shell & more


if not os.path.isdir(".pnpm/icona"):
    icona_repo = "git@github.com:robo-monk/ICONA.git"
    shell(f"git clone {icona_repo} .pnpm/icona", shell=True) # shell("ls") will run ls inside a shell terminal


# build icons
c = spawn(f"Bundling icons...") # this will produce a beatiful process log
# ...
c.done() # close the process and show how much time it took

c = spawn(f"Bundling with {package_manager}...")

shell(f"{config('package_manager')} run build")
  # config(key) accesses the values located in .pnpm/config.yml
c.done()

```

