import os

def do_ls(self, args):
    import os
    files = os.listdir('.')
    print('\n'.join(files))

def help_ls(self):
    """
    Usage: ls
    List files in the current directory
    """