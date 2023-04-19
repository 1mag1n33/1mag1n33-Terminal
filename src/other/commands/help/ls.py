import os


def do_ls(self, args):
    """
    List files and directories in the current directory.
    """
    if args:
        path = args
    else:
        path = '.'

    if not os.path.isdir(path):
        print(f"'{path}' is not a directory.")
        return

    files = os.listdir(path)
    print('\n'.join(files))
    
def help_ls(self):
    """
    Display detailed help for the ls command.
    """
    print("List files and directories in the current directory.\n")
    print("Usage: ls [directory]")
    print("  directory: Optional. The directory to list. Defaults to the current directory.")
