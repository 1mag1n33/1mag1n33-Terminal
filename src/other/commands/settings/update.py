def do_update(self, args):
    import argparse
    import json
    import os
    from src.other.commands import settings
    print(settings)
    
    parser = argparse.ArgumentParser(prog='update')
    subparsers = parser.add_subparsers(dest='command')
    
    autoupdate_parser = subparsers.add_parser('autoupdate')
    autoupdate_parser.add_argument('autoupdate_status', nargs='?' ,type=str, help='Set autoupdate status (True or False)')
    
    parsed_args = parser.parse_args(args.split())
    
    if parsed_args.command == 'autoupdate':
        # parse autoupdate sub-command argument

        with open(settings, 'r') as f:
            server_config = json.load(f)
        

        autoupdate_status = parsed_args.autoupdate
        if autoupdate_status is None:
            # print current autoupdate value
            autoupdate_status = server_config.get('autoupdate', True)
            print(f"Current Autoupdate value is {autoupdate_status}")
        elif autoupdate_status.lower() in ['true', 'false']:
            # set new autoupdate value
            server_config['autoupdate'] = autoupdate_status.lower() == 'true'
            with open(settings, 'w') as f:
                json.dump(server_config, f)
            print(f"Autoupdate value set to {autoupdate_status.lower() == 'true'}")
        else:
            print("Invalid input. Please enter 'True' or 'False'.")