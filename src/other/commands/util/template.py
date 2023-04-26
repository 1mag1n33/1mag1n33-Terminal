import argparse
import os
import shutil
import sys
from tqdm import tqdm

#Global Variables

req_files = ['requirements.txt', 'req.txt', 'reqs.txt']

templates_path = 'templates'

def do_template(self, args):
    # Create the "templates" folder if it doesn't exist
    if not os.path.exists(templates_path):
        os.mkdir(templates_path)

    #args

    parser = argparse.ArgumentParser(description="Copies files from the specified template folder to the current working directory.")
    parser.add_argument(
        'folder',
        nargs='?',
        type=str,
        help="Enter the name of the folder to copy"
    )

    parser.add_argument(
        '-S',
        '--specify-file',
        type=str,
        help="Specify a file to copy from the template folder"
    )

    parser.add_argument(
        '-L', '--list',
        action='store_true',
        help="List all the available templates"
    )


    args = parser.parse_args()

    #logic

    if templates_path is None:
        print("Could not find the templates folder.")
    else:
        if args.list:
            print("Available templates:")
            for template_dir in os.listdir(templates_path):
                if os.path.isdir(os.path.join(templates_path, template_dir)):
                    print(f" - {template_dir}")

        else:
            if args.folder is None:
                print("Please provide a template folder name or use the -L/--list option to list available templates.")
            else:
                folder_path = os.path.join(templates_path, args.folder)

                if not os.path.isdir(folder_path):
                    print(f"{folder_path} is not a valid directory.")
                else:
                    dest_dir = os.path.join(os.getcwd(), args.folder)
                    if os.path.exists(dest_dir):
                        # If the destination directory already exists, delete it
                        shutil.rmtree(dest_dir)

                    file_count = sum(len(files) for _, _, files in os.walk(folder_path))
                    if args.specify_file:
                        filepath = os.path.join(folder_path, args.specify_file)
                        if os.path.isfile(filepath):
                            shutil.copy2(filepath, os.getcwd())
                            print(f"Copied {args.specify_file} to {os.getcwd()}.")
                        else:
                            print(f"{args.specify_file} does not exist in {folder_path}")
                    else:
                        with tqdm(total=file_count, desc="Copying files") as pbar:
                            for root, dirs, files in os.walk(folder_path):
                                for file in files:
                                    src_path = os.path.join(root, file)
                                    dest_path = os.path.join(dest_dir, os.path.relpath(src_path, folder_path))
                                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                                    shutil.copy2(src_path, dest_path)
                                    pbar.update(1)
                        print(f"Copied {args.folder} to {os.getcwd()}.")
                    
                    # Check if the requirements files exist and install the packages if found
                    req_found = False
                    for req_file in req_files:
                        if req_file in os.listdir(folder_path):
                            req_found = True
                            break

                    if req_found:
                        venv_path = os.path.join(dest_dir, '.venv')
                        if not os.path.exists(venv_path):
                            os.makedirs(venv_path)
                            print(f"Created {venv_path} directory.")

                    # Create and activate the virtual environment
                        os.system(f"python -m venv {venv_path}")
                        activate_path = os.path.join(dest_dir, ".venv", "Scripts", "activate.bat")
                        os.system(f"\"{activate_path}\"")
                        print(f"Activated {activate_path} directory.")
                        print(f"Checking for requirements files in {folder_path}/{req_file}")

                        # Install the required packages using pip
                        installed_pkgs = []
                        with tqdm(total=100, desc="Installing packages") as pbar:
                            for req_file in req_files:
                                req_path = os.path.join(folder_path, req_file)
                                if os.path.isfile(req_path):
                                    req_install = f"{os.getcwd()}\{args.folder}\{req_file}"
                                    os.system(f"pip install -r {req_install}")
                                    with open(req_path, 'r') as f:
                                        pkgs = f.read().splitlines()
                                    installed_pkgs += pkgs
                                    break  # Install only the first requirements file found
                                pbar.update(100 - pbar.n)
                        print(f"Installed packages: {', '.join(installed_pkgs)}")
