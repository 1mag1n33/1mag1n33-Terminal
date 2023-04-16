import os
import cmd
import importlib
import pkgutil

class Terminal(cmd.Cmd):
    def __init__(self, write_output=None):
        super().__init__()
        self.write_output = write_output or print
        self.intro = "Welcome to the 1mag1n33 Terminal. Type help or ? to list commands.\n"
        self.prompt = f"{os.getcwd()}\n$ "

        self.groups = {}

        self.load_commands()

    def load_commands(self):
        base_dir = 'src.other.commands'
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for filename in filenames:
                if filename.endswith('.py'):
                    module_name = os.path.splitext(filename)[0]
                    module_path = os.path.join(dirpath, filename).replace(os.sep, '.')
                    module = importlib.import_module(module_path)
                    function_name = f'do_{module_name}'
                    if hasattr(module, function_name):
                        command_func = getattr(module, function_name)
                        setattr(Terminal, command_func.__name__, command_func)
                        group = dirpath.split(os.sep)[-1]
                        self.groups.setdefault(group, [])
                        self.groups[group].append(module_name)
                        help_func = getattr(module, f'help_{module_name}', None)
                        if help_func:
                            setattr(self.__class__, f'help_{module_name}', help_func)

    def do_help(self, args):
        if args:
            try:
                func = getattr(self, 'help_' + args)
            except AttributeError:
                print(f'No help found for "{args}"')
            else:
                print(func.__doc__)
        else:
            for group, commands in self.groups.items():
                print(f'{group.capitalize()}:')
                print('\n'.join(f'\t{command}' for command in commands))
                
    def help_help(self):
        """
        Usage: ?, help
        Gives you a list of the commands.
        """

    def do_exit(self, args=None):
        """
        Exits the terminal
        """
        print('Exiting the terminal...')
        raise SystemExit
