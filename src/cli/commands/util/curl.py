import requests
import argparse

def do_curl(self, args):
    """send a GET request to the specified URL and retrieve the response."""
    parser = argparse.ArgumentParser(prog='curl')
    parser.add_argument('url', help='the URL to fetch')
    parser.add_argument('-o', dest='output', help='output file')
    parsed_args = parser.parse_args(args.split())

    url = parsed_args.url
    output_file = parsed_args.output

    response = requests.get(url)

    if output_file:
        with open(output_file, 'wb') as f:
            f.write(response.content)
            print(f"Downloaded to {output_file}")
    else:
        print(response.text)
