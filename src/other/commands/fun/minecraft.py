def do_minecraft(self, args):
    import argparse
    import json
    import os
    from src.other.commands.fun.Minecraft._create import Create
    from src.other.commands.fun.Minecraft._run import Run

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
            
        # prompt for port
        port = input(f"Enter port number (default: 25565): ")
        if not port:
            port = 25565
        else:
            port = int(port)
        
        # write values to JSON file
        with open(server_path, 'w') as f:
            json.dump({'version': version, 'server_name': server_name, 'memory': memory, 'port': port}, f)
                
        # create the server
        Create().generate_files()
        print(f"Creating Minecraft server version {version} with name {server_name} with mem {memory}")
        
    elif parsed_args.command == 'run':
        # load values from JSON file
        with open(server_path, 'r') as f:
            server_config = json.load(f)
        
        # get port number from the JSON file
        port = server_config.get('port', 25565)
        
        port_number = input(f"Enter port number (default: {port}): ")
        if not port_number:
            port_number = port
        else:
            port_number = int(port_number)
            server_config['port'] = port_number
            with open(server_path, 'w') as f:
                json.dump(server_config, f)
        
        
        self.path = f'Mc_Servers/{Create().server_name}'
        
        Run.Start(self)
        
        print(f"Running Minecraft server on port {port_number}")
    else:
        print("Invalid command")
