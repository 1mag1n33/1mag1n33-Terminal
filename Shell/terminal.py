import cmd
import os
from importlib import import_module

class Terminal(cmd.Cmd):
    intro = "Welcome to the 1mag1n33 Terminal. Type help or ? to list commands.\n"
    prompt = '1mag1n33 $ '

    def __init__(self):
        super().__init__()
        self.load_commands()

    def load_commands(self):
        command_dir = os.path.join(os.path.dirname(__file__), 'commands')
        for filename in os.listdir(command_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module = import_module(f'shell.commands.{module_name}')
                command_name = f'do_{module_name}'
                command_func = getattr(module, command_name)
                setattr(Terminal, command_name, command_func)

    def do_help(self, args):
        """List available commands with "help" or detailed help with "help cmd"."""
        if args:
            try:
                func = getattr(self, 'help_' + args)
            except AttributeError:
                print(f'No help found for "{args}"')
            else:
                print(func.__doc__)
        else:
            commands = [cmd[3:] for cmd in dir(self) if cmd.startswith('do_')]
            print('\n'.join(commands))