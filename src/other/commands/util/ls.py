import os
from termcolor import colored


def list_dir(path, indent='   '):
    """
    Recursively list the contents of directories.
    """
    files = os.listdir(path)
    for filename in sorted(files):
        if not filename.startswith('.'):
            full_path = os.path.join(path, filename)
            if os.path.isdir(full_path):
                print(f"{indent} {colored(filename, 'blue')}/")
                list_dir(full_path, indent + "  ")
            else:
                if not filename.startswith('.'):
                    print(f"{indent}  - {colored(filename, 'yellow')}")


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

    foldername = os.path.basename(os.getcwd())
    
    print(f"Contents of {colored(foldername, 'green')}:")
    list_dir(path, "")
