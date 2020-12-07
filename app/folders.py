import os
import ast
from pathlib import Path

Directory = os.path.join(Path.home(), '.sdlm')
if os.path.exists(Directory) == False:
    os.mkdir(Directory)

File = os.path.join(Directory, 'folders.json')


def _exist():
    return os.path.exists(File)


def _read():
    if os.path.exists(File):
        file = open(File, 'r')
        data = str(file.read())
        if data[0:1] != '[' or data[-1] != ']':
            del file
            return list()
        else:
            try:
                data = ast.literal_eval(data)
                file.close()
                del file
                return data
            except:
                print("{0} file is corrupted!".format(str(File)))
                exit(1)
    else:
        return list()


def add(folder):
    if remove(folder):
        data = _read()
        data.append(folder)
        file = open(File, 'w')
        file.write(str(data))
        file.close()
        del file
        del data
        return True


def remove(folder):
    data = _read()
    if len(data) == 0:
        return True
    if folder in data:
        index = data.index(folder)
        del data[index]
        file = open(File, 'w')
        file.write(str(data))
        file.close()
        del file
        del index
        del data
    return True
