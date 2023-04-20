import os

def do_cd(self, arg):
        """Change the current working directory."""
        try:
            if arg:
                os.chdir(os.path.abspath(arg))
            else:
                os.chdir(os.path.expanduser("~"))
        except OSError as e:
            print(f"Error: {e}")
        self.prompt = f"{os.getcwd()}\n$ "

