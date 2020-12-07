import os

def start(path):
    os.popen('aria2c --input-file={0} -c'.format(path))
    print("Start downloading via aria2c")