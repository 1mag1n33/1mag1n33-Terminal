import os

def do_pwd(self, args):
    print(os.getcwd())

def help_pwd(self):
    """
    Usage: pwd
    Print the current working directory.
    """