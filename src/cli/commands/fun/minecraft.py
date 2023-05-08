def do_minecraft(self, args):
    """Does minecraft things"""
    import argparse
    import json
    import os
    from src.cli.support_files.Minecraft._create import Create
    from src.cli.support_files.Minecraft._run import Run

    parser = argparse.ArgumentParser(prog='minecraft')
    subparsers = parser.add_subparsers(dest='command')

    # Sub Commands
    
    backup_parser = subparsers.add_parser('backup')
    backup_parser.add_argument('backup_status', nargs='?' ,type=str, help='Set backup status (True or False)')
    
    update_parser = subparsers.add_parser('update')
    backup_parser.add_argument('update_status', nargs='?' ,type=str, help='Set backup status (True or False)')
    
    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('--port', '-p', type=int, default=25565)
    
    create_parser = subparsers.add_parser('create')

    # parse the arguments
    parsed_args = parser.parse_args(args.split())

    server_path = 'src/other/support_files/Minecraft/server_config.json'
    
    with open(server_path, 'r') as f:
                server_config = json.load(f)
    


        # handle the sub-commands
    if parsed_args.command == 'create':
        # prompt for version
        version = input(f"Enter Minecraft version (default: {server_config['version']}): ")
        if not version:
            version = server_config['version']
        
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
        
        server_config['version'] = version
        server_config['server_name'] = server_name
        server_config['memory'] = memory
        server_config['port'] = port
                
        with open(server_path, 'w') as f:
            json.dump(server_config, f, indent=4, sort_keys=True)
            
            
                
        # create the server
        Create().generate_files()
        print(f"Creating Minecraft server version {version} with name {server_name} with mem {memory}")
        
    elif parsed_args.command == 'run':
        # load values from JSON file
        try:
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
                    json.dump(server_config, f, indent=4, sort_keys=True)
            
            self.path = f'Mc_Servers/Servers/{Create().server_name}'
            backup_enabled = server_config.get('backup', True)
            Run.Start(self, backup_enabled)
        
        except FileNotFoundError:
            print(f"Minecraft server with name '{Create().server_name}' not found")
            
    elif parsed_args.command == 'backup':
        # parse backup sub-command argument

        with open(server_path, 'r') as f:
            server_config = json.load(f)

        backup_status = parsed_args.backup_status
        if backup_status is None:
            # print current backup value
            backup_status = server_config.get('backup', True)
            print(f"Current backup value is {backup_status}")
        elif backup_status.lower() in ['true', 'false']:
            # set new backup value
            server_config['backup'] = backup_status.lower() == 'true'
            with open(server_path, 'w') as f:
                json.dump(server_config, f, indent=4, sort_keys=True)
            print(f"Backup value set to {backup_status.lower() == 'true'}")
        else:
            print("Invalid input. Please enter 'True' or 'False'.")
            
    elif parsed_args.command == 'update':
        with open(server_path, 'r') as f:
            server_config = json.load(f)

        update_status = parsed_args.update_status
        if update_status is None:
            # print current backup value
            update_status = server_config.get('update', True)
            print(f"Current backup value is {update_status}")
        elif update_status.lower() in ['true', 'false']:
            # set new backup value
            server_config['update'] = update_status.lower() == 'true'
            with open(server_path, 'w') as f:
                json.dump(server_config, f, indent=4, sort_keys=True)
            print(f"Updater value set to {update_status.lower() == 'true'}")
        else:
            print("Invalid input. Please enter 'True' or 'False'.")
    else:
        print("Invalid command")
