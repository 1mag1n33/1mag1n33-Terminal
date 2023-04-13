import os
import importlib

class GitBash:
    def __init__(self):
        self.commands = self.load_commands()

    def load_commands(self):
        """Load built-in commands from the commands directory"""
        commands = {}
        for file in os.listdir('commands'):
            if file.endswith('_command.py'):
                module_name = file[:-3]
                module = importlib.import_module(f'commands.{module_name}')
                execute_func = getattr(module, f'get_do_{module_name}')()  # Call the get_do_{command} function to get the do_{command} function
                commands[module_name] = execute_func
        return commands

