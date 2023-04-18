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
                        help_func = getattr(module, f'help_{module_name}', None)
                        if help_func:
                            setattr(self.__class__, f'help_{module_name}', help_func)

