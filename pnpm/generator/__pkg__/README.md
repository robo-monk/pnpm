# __pkg__ 
![npm-size](https://img.shields.io/npm/v/__pkg__?style=flat-square)
![npm-size](https://img.shields.io/github/commit-activity/m/__git_username__/__pkg?style=flat-square)
![npm-size](https://img.shields.io/npm/dw/__pkg__?style=flat-square)

### [ 🚀 Demo ](https://__git_username__.github.io/__pkg__)

* made with ❤ ️by __git_username__ *

## First time:

```bash
git clone git@github.com:__git_username__/__pkg__.git
cd __pkg__
pnpm dev -r # reload dependencies
```

* Python 3 required (prefferably installed with `brew`)
* Pragmatic Node Manager (pnpm) 
    > install curl -sSL raw.githubusercontent.com/robo-monk/pnpm/master/copy%2Bpaste.py | python3 - && zsh

## Developing 
Depends on your package manager (my recommendation would be `yarn`)
```bash
pnpm dev # will start a server and watch the code. Will
         # also check whether tests pass if configed so;
```

```bash
pnpm release # will release the package to npm repository

# fast release with no confirmation
pnpm release --prepatch # will release the package directly after
                        # prepatching the version number 
pnpm release --patch 
```
