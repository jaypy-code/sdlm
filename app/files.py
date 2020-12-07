import os

name = ".sdlm-links.txt"

def getPath():
    return os.path.join(os.getcwd(), name)

def create(links):
    path = getPath()
    links = '\n'.join(links)
    file = open(path, 'w')
    file.write(links)
    file.close()
    del file
    del links
    return path


def exists():
    return os.path.exists(getPath())