import os
import importlib
import pickle
import inspect
import click

def load_commands(commands_by_folder, Terminal):
    # Load commands from the directory
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
                        if isinstance(value, click.Command):
                            add_command(value, commands_by_folder, dirpath, package, Terminal)
                except Exception as e:
                    print(f"Failed to load module {modname} from {module_path}: {e}")

def add_command(cmd, commands_by_folder, dirpath, package, Terminal):
    cmd_name = cmd.name

    def command_wrapper(*args, **kwargs):
        try:
            cmd.main(args=list(args), standalone_mode=False, **kwargs)
        except Exception as e:
            print(f"Error executing command: {str(e)}")

    setattr(Terminal, f"do_{cmd_name}", command_wrapper)

    # Add the command to the dictionary of commands by folder
    folder_name = os.path.relpath(dirpath, package)
    commands_by_folder.setdefault(folder_name, [])
    commands_by_folder[folder_name].append(cmd_name)
