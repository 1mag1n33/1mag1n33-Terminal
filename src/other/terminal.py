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

    

    
    def do_help(self, args):
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
    
    def help_help(self):
        """
        Usage: ?, help
        Gives u a list of the commands.
        """

    def load_commands(self):
        package = 'src.other.commands'
        for _, module_name, _ in pkgutil.iter_modules([package.replace('.', '/')]):
            # Import the module
            module = importlib.import_module(f'{package}.{module_name}')
            # Get the function name from the module name
            function_name = f'do_{module_name.split(".")[-1]}'
            # Check if the function exists in the module
            if hasattr(module, function_name):
                # If it exists, get the function and add it as a command
                command_func = getattr(module, function_name)
                setattr(Terminal, command_func.__name__, command_func)
                
                help_func = getattr(module, f'help_{module_name}', None)
                if help_func:
                    setattr(self.__class__, f'help_{module_name}', help_func)
                    
    # Exit command
    def do_exit(self, args=None):
        """
        Exits the terminal
        """
        print('Exiting the terminal...')
        raise SystemExit