import os

def do_mkfile(self, arg):
    
    CONFIG_FILE = (arg)
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w'):
            pass