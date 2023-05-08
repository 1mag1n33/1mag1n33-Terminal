import os
from colored import fg, bg, attr

prompt_color = fg('green')
text_color = fg('white')
reset = attr('reset')
def do_cd(self, arg):
        """Change the current working directory."""
        try:
            if arg:
                os.chdir(os.path.abspath(arg))
            else:
                os.chdir(os.path.expanduser("~"))
        except OSError as e:
            print(f"Error: {e}")
        self.prompt = f"{prompt_color}{os.getcwd()}\n{reset}$ "

