import argparse
import os
import shutil
import zipfile
import requests
from src.other.util.progressbar.progress import ProgressBar

def do_website(self, args):
    parser = argparse.ArgumentParser(prog='website')
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('flask')
    parsed_args = parser.parse_args(args.split())

    if parsed_args.command == 'flask':
        url = 'https://terminaldevlopment.000webhostapp.com/src/flask.zip'
        filename = url.split('/')[-1]
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024 # 1 Kibibyte
        

        with open(filename, 'wb') as f:
            for data in response.iter_content(block_size):
                ProgressBar.update(data ,'Flask', 'Complete')
                f.write(data)

        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())

        os.remove(filename)
