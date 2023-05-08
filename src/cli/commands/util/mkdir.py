import os

def do_mkdir(self, arg):
    """Create a directory"""
    path = os.path.join(os.getcwd(),arg)
    os.makedirs(path)