import os
import cmd
import importlib
import pickle
from colored import fg, attr
import multiprocessing
import inspect

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
        self.commands_by_folder = {}

        # Load the commands
        self.load_commands()


    def load_commands(self):
        # Check if pickle file exists
        if os.path.exists('command_state.pickle'):
            with open('command_state.pickle', 'rb') as f:
                self.commands_by_folder = pickle.load(f)
        else:
            # Load commands from the directory
            self.load_commands_from_directory()

    def load_commands_from_directory(self):
        package = 'src.cli.commands'
        for dirpath, dirnames, filenames in os.walk(package):
            # Remove subdirectories from dirnames so they're not processed again
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for filename in filenames:
                if not filename.endswith('.py') or filename.startswith('_'):
                    continue
                elif filename.startswith('cmd_'):
                    modname = os.path.splitext(filename)[0]
                    module_path = os.path.join(dirpath, filename)
                    try:
                        module = importlib.import_module(
                            f'src.cli.commands.{os.path.relpath(module_path, package)[:-3].replace(os.path.sep, ".")}'
                        )
                        for name, value in inspect.getmembers(module):
                            if inspect.isfunction(value):
                                self.add_command(value)
                                # Add the command to the dictionary of commands by folder
                                folder_name = os.path.relpath(dirpath, package)
                                self.commands_by_folder.setdefault(folder_name, [])
                                self.commands_by_folder[folder_name].append(name)
                    except Exception as e:
                        print(f"Failed to load module {modname} from {module_path}: {e}")

    def add_command(self, cmd_func):
        def command_wrapper(*args, **kwargs):
            try:
                cmd_func(*args, **kwargs)
            except Exception as e:
                print(f"Error executing command: {str(e)}")

        cmd_name = cmd_func.__name__[4:]
        setattr(self.__class__, f"do_{cmd_name}", command_wrapper)

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
            for folder, commands in self.commands_by_folder.items():
                if folder:
                    print(f"\n  {group_color}{folder}{reset}:")
                else:
                    print()
                for cmd in commands:
                    cmd_name = cmd[4:]
                    func = getattr(self.__class__, f"do_{cmd_name}")
                    doc = func.__doc__ or ''
                    description = doc.strip().split('\n')[0]
                    print(f"    - {help_color}{cmd_name}{reset}: {desc_color}{description}{reset}")

