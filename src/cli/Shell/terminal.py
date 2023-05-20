import os
import cmd
import importlib
import pickle
from colored import fg, attr
import multiprocessing
import inspect
from src.cli.Shell.command_loader import load_commands,commands_by_folder

# main colors
prompt_color = fg('green')
text_color = fg('white')
reset = attr('reset')

# help colors
help_color = fg('yellow')
group_color = fg('blue')
desc_color = fg('red')

class Terminal(cmd.Cmd):
    intro = "Welcome to the 1mag1n33 Terminal. Type help or ? to list commands.\n"
    prompt = f"{prompt_color}{os.getcwd()}\n{reset}$ "
    def __init__(self):
        super().__init__()

        # Dictionary to hold the commands organized by folder

        load_commands(self)


    # Help command
        # Help command
    def do_help(self, arg):
        """List available commands."""
        if arg:
            if hasattr(self.__class__, f"do_{arg}"):
                func = getattr(self.__class__, f"do_{arg}")
                doc = func.__doc__ or ''
                description = doc.strip().split('\n')[0]
                print(description)
            else:
                print(f"Unknown command '{arg}'")
        else:
            print("Available commands:")
            for folder, commands in commands_by_folder.items():
                if folder:
                    print(f"\n  {group_color}{folder}{reset}:")
                else:
                    print()
                for cmd in commands:
                    func = getattr(self.__class__, cmd)
                    doc = func.__doc__ or ''
                    description = doc.strip().split('\n')[0]
                    print(f"    - {help_color}{cmd[3:]}{reset}: {desc_color}{description}{reset}")
            print('\n')


