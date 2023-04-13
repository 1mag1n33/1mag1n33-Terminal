import os
import sys
import cmd
from cmd.mycmd import MyCmd

def load_commands(cmd):
    """
    Load built-in commands from the commands/ directory.
    """
    import importlib.util
    from cmd.commands.base_command import BaseCommand

    commands_dir = os.path.join(os.path.dirname(__file__), "cmd/commands")
    for filename in os.listdir(commands_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = os.path.splitext(filename)[0]
            module_path = os.path.join(commands_dir, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and issubclass(obj, BaseCommand) and obj is not BaseCommand:
                    cmd.register_command(obj())

class MyTerminal(MyCmd):
    intro = 'Welcome to the 1mag1n33 Terminal. Type help or ? to list commands.\n'
    prompt = '> '

if __name__ == '__main__':
    cmd = MyTerminal()
    load_commands(cmd)
    cmd.cmdloop()
