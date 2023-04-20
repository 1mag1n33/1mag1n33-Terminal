import os

def do_mkdir(self, arg):
    path = os.path.join(os.getcwd(),arg)
    os.makedirs(path)