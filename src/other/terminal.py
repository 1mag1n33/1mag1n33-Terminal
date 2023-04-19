import os
import cmd
import importlib
import pkgutil

class Terminal(cmd.Cmd):
    intro = "Welcome to the 1mag1n33 Terminal. Type help or ? to list commands.\n"
    prompt = f"{os.getcwd()}\n$ "

    def __init__(self):
        super().__init__()
        
        # Dictionary to hold the commands organized by folder
        self.commands_by_folder = {}

        # Load the commands
        self.load_commands()

    def load_commands(self):
        package = 'commands'
        for _, module_name, ispkg in pkgutil.iter_modules([package]):
            if not ispkg:
                # If the module is not a package, import it directly
                # Import the module
                module = importlib.import_module(f'{package}.{module_name}')
                # Get the function name from the module name
                function_name = f'do_{module_name.split(".")[-1]}'
                # Check if the function exists in the module
                if hasattr(module, function_name):
                    # If it exists, get the function and add it as a command
                    command_func = getattr(module, function_name)
                    setattr(Terminal, command_func.__name__, command_func)
                    # Add the command to the dictionary of commands by folder
                    folder_name = os.path.relpath(os.path.dirname(module.__file__), package)
                    self.commands_by_folder.setdefault(folder_name, [])
                    self.commands_by_folder[folder_name].append(command_func.__name__)
                    
                    # Add the help command for the command
                    help_func = getattr(module, f'help_{module_name}', None)
                    if help_func:
                        setattr(self.__class__, f'help_{command_func.__name__}', help_func)

    # Help command
    def do_help(self, args=None):
        """
        List available commands with "help" or detailed help with "help cmd".
        """
        if args:
            # Display detailed help for the specified command
            try:
                func = getattr(self, f'help_{args}')
            except AttributeError:
                func = None
            if func:
                func()
            else:
                print(f"No help found for command '{args}'.")
        else:
            # Display list of available commands organized by folder
            print("Available commands:")
            for folder, commands in self.commands_by_folder.items():
                if folder:
                    print(f"\n{folder}:")
                for command in commands:
                    print(f"\t{command}")
