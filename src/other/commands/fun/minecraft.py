def do_minecraft(self, args):
    import argparse
    import json
    from src.other.commands.fun.Minecraft._create import Create

    parser = argparse.ArgumentParser(prog='minecraft')
    subparsers = parser.add_subparsers(dest='command')

    # create sub-command
    create_parser = subparsers.add_parser('create')

    # run sub-command
    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('--port', '-p', type=int, default=25565)

    # parse the arguments
    parsed_args = parser.parse_args(args.split())

    server_path = 'src/other/support_files/server_config.json'
    
    # handle the sub-commands
    if parsed_args.command == 'create':
        # prompt for version
        version = input("Enter Minecraft version (default: latest): ")
        if not version:
            version = 'latest'
        
        # prompt for server name
        server_name = input("Enter server name (default: minecraft_server): ")
        if not server_name:
            server_name = 'minecraft_server'
        
        # prompt for memory
        memory = input("Enter memory in MB (default: 4000): ")
        if not memory:
            memory = 4000
        else:
            memory = int(memory)
        
        # write values to JSON file
        with open(server_path, 'w') as f:
            json.dump({'version': version, 'server_name': server_name, 'memory': memory}, f)
                
        # create the server
        Create().generate_files()
        print(f"Creating Minecraft server version {version} with name {server_name} with mem {memory}")
    elif parsed_args.command == 'run':
        port = parsed_args.port
        # do something with the arguments
        print(f"Running Minecraft server on port {port}")
    else:
        print("Invalid command")
