def do_debug(self, args):
    import argparse
    import json
    from src.imports import settings
    
    parser = argparse.ArgumentParser(prog='debug')
    parser.add_argument('debug_status', nargs='?' ,type=str, help='Set debug status (True or False)')
    
    parsed_args = parser.parse_args(args.split())
    
    with open(settings, 'r') as f:
        settings_config = json.load(f)

    if parsed_args.debug_status:
        # parse autoupdate sub-command argument
        

        debug_status = parsed_args.debug_status
        if debug_status.lower() in ['true', 'false']:
            # print current autoupdate value
            settings_config['debug'] = debug_status.lower() == 'true'
            with open(settings, 'w') as f:
                json.dump(settings_config, f, indent=4, sort_keys=True)
            print(f"debug value set to {debug_status.lower() == 'true'}")
        else:
            print("Invalid input. Please enter 'True' or 'False'.")
            
    elif parsed_args.debug_status is None:
        print(f"debug value set to {settings_config.get('debug', True)}")
