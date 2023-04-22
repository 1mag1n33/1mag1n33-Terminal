# minecraft.py

import argparse
from src.other.supports_files.Minecraft._create import Create

# define the variables outside the function
version = ''
server_name = ''
memory = ''

def do_minecraft(self, args):
    global version, server_name

    parser = argparse.ArgumentParser(prog='minecraft')
    subparsers = parser.add_subparsers(dest='command')

    # create sub-command
    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('version', type=str)
    create_parser.add_argument('--mem', '-m', type=int, default=4000)
    create_parser.add_argument('--name', '-n', type=str, default='minecraft_server')
    
    # run sub-command
    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('--port', '-p', type=int, default=25565)

    # parse the arguments
    parsed_args = parser.parse_args(args.split())

    # handle the sub-commands
    if parsed_args.command == 'create':
        version = parsed_args.version
        server_name = parsed_args.name
        memory = parsed_args.mem
        # do something with the arguments
        Create()
        print(f"Creating Minecraft server version {version} with name {server_name} with mem {memory}")
    elif parsed_args.command == 'run':
        port = parsed_args.port
        # do something with the arguments
        print(f"Running Minecraft server on port {port}")
    else:
        print("Invalid command")
