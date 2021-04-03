import site

def abs_path(sub=''):
    return site.getsitepackages()[0] + '/pnpm' + sub
