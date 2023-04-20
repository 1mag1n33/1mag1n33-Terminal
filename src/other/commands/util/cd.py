import os

def do_cd(self, arg):
        """Change the current working directory."""
        try:
            os.chdir(arg)
        except Exception as e:
            print(f"Error: {e}")

