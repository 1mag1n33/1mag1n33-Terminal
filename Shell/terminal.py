import os
import cmd
import importlib

class Terminal(cmd.Cmd):
    intro = "Welcome to the 1mag1n33 Terminal. Type help or ? to list commands.\n"
    prompt = '1mag1n33 $ '

    def __init__(self):
        super().__init__()

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

    def load_commands(self):
        commands_dir = os.path.join(os.getcwd(), 'shell\commands')
        for filename in os.listdir(commands_dir):
            if filename.endswith('.py'):
                module_name = filename[:-3]
                module = importlib.import_module(f'shell.commands.{module_name}')
                command_name = module_name.replace('_', '-')
                command_func = getattr(module, f'do_{module_name}')
                setattr(Terminal, f'do_{command_name}', command_func)