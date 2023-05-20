import os
import importlib

commands_by_folder = {}

def load_commands(self):
        package = 'src/cli/commands'
        for dirpath, dirnames, filenames in os.walk(package):
            # Remove subdirectories from dirnames so they're not processed again
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for filename in filenames:
                if not filename.endswith('.py') or filename.startswith('_'):
                    continue
                modname = os.path.splitext(filename)[0]
                module_path = os.path.join(dirpath, filename)
                try:
                    module = importlib.import_module(f'src.cli.commands.{os.path.relpath(module_path, package)[:-3].replace(os.path.sep, ".")}')
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
                        commands_by_folder.setdefault(folder_name, [])
                        commands_by_folder[folder_name].append(cmd_name)
