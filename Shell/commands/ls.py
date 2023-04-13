import os

def do_ls(args):
    """List files in the current directory"""
    print('\n'.join(os.listdir(args)))
