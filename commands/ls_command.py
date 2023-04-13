import os

def do_ls(args):
    """List files in the current directory"""
    print('\n'.join(os.listdir(args)))
    
def get_do_ls():
    """Returns the do_ls function"""
    return do_ls
