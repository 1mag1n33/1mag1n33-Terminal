import os

def do_mkfile(self, arg):
    """Create a file"""
    CONFIG_FILE = (arg)
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w'):
            pass