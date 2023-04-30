def do_website(self, args):
    import argparse
    import shutil
    import os
    import datetime
    
    parser = argparse.ArgumentParser(prog='website')
    subparsers = parser.add_subparsers(dest='command')
    
    subparsers.add_parser('flask')
    
    parsed_args = parser.parse_args(args.split())
    
    
    if parsed_args.command == 'flask':
        src_dir = os.path.abspath('src/other/support_files/website/flask')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        dest_dir = os.path.join(os.getcwd(), f'flask_{timestamp}')
        shutil.copytree(src_dir, dest_dir)