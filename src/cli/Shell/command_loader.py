import os
import importlib
import pickle
import inspect

def load_commands(commands_file, Terminal):
    # Load commands from the directory
    print(Terminal)
    package = 'src.cli.commands'
    commands_by_folder = {}
    
    for dirpath, dirnames, filenames in os.walk(package):
        # Remove subdirectories from dirnames so they're not processed again
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        print(dirpath, dirnames, filenames)  # Print the directory information
        
        for filename in filenames:
            if not filename.endswith('.py') or filename.startswith('_'):
                continue
            elif filename.startswith('cmd_'):
                modname = os.path.splitext(filename)[0]
                module_path = os.path.join(dirpath, filename)
                print(f"Loading module {modname} from {module_path}")
                
                try:
                    module = importlib.import_module(
                        f'src.cli.commands.{os.path.relpath(module_path, package)[:-3].replace(os.path.sep, ".")}'
                    )
                    
                    for name, value in inspect.getmembers(module):
                        if inspect.isfunction(value):
                            add_command(value, commands_by_folder, dirpath, package, Terminal)
                            
                except Exception as e:
                    print(f"Failed to load module {modname} from {module_path}: {e}")

    with open(commands_file, 'wb') as f:
        pickle.dump(commands_by_folder, f)

def add_command(cmd_func, commands_by_folder, dirpath, package, Terminal):
    def command_wrapper(*args, **kwargs):
        try:
            cmd_func(*args, **kwargs)
        except Exception as e:
            print(f"Error executing command: {str(e)}")

    cmd_name = cmd_func.__name__[4:]
    setattr(Terminal, f"do_{cmd_name}", command_wrapper)

    # Add the command to the dictionary of commands by folder
    folder_name = os.path.relpath(dirpath, package)
    commands_by_folder.setdefault(folder_name, [])
    commands_by_folder[folder_name].append(cmd_name)
    print(f"Command '{cmd_name}' loaded from folder '{folder_name}'")
