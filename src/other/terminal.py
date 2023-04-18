import os
import cmd
import importlib
import pkgutil

class Terminal(cmd.Cmd):
    intro = "Welcome to the 1mag1n33 Terminal. Type help or ? to list commands.\n"
    prompt = f"{os.getcwd()}\n$ "

    def __init__(self):
        super().__init__()

    def load_commands(self):
        package = 'src.commands'
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