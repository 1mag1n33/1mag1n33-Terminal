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
    