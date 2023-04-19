import os
import cmd
import importlib

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
        package = 'src/other/commands'
        for dirpath, dirnames, filenames in os.walk(package):
            # Remove subdirectories from dirnames so they're not processed again
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for filename in filenames:
                if not filename.endswith('.py') or filename.startswith('_'):
                    continue
                modname = os.path.splitext(filename)[0]
                module_path = os.path.join(dirpath, filename)
                try:
                    module = importlib.import_module(f'src.other.commands.{os.path.relpath(module_path, package)[:-3].replace(os.path.sep, ".")}')
                except Exception as e:
                    print(f"Failed to load module {modname} from {module_path}: {e}")
                    continue
                for obj in dir(module):
                    if obj.startswith('do_'):
                        cmd_name = obj
                        cmd_func = getattr(module, obj)
                        setattr(self.__class__, cmd_name, cmd_func)
                        # Add the command to the dictionary of commands by folder
                        folder_name = os.path.relpath(dirpath, package)
                        self.commands_by_folder.setdefault(folder_name, [])
                        self.commands_by_folder[folder_name].append(cmd_name)
                        # Check for a help function
                        help_func = getattr(module, f'help_{cmd_name[3:]}', None)
                        if help_func:
                            setattr(self.__class__, f'help_{cmd_name[3:]}', help_func)
                        print(f"Command {cmd_name[3:]} loaded from folder {folder_name}")
        print("Commands loaded:")
        print(self.commands_by_folder)

    # Help command
    def do_help(self, arg):
        """List available commands."""
        if arg:
            try:
                func = getattr(self, f'help_{arg}')
            except AttributeError:
                func = None
            if func:
                func()
            else:
                print(f"No help found for command '{arg}'.")
        else:
            print("Available commands:")
            for folder, commands in self.commands_by_folder.items():
                if folder:
                    print(f"\n{folder}:")
                else:
                    print()
                for cmd in commands:
                    # Get the function object for the command
                    func = getattr(self.__class__, cmd)
                    # Get the docstring for the function
                    doc = func.__doc__ or ''
                    # Extract the first line of the docstring (if any) as the command description
                    description = doc.strip().split('\n')[0]
                    print(f" - {cmd[3:]}: {description}")