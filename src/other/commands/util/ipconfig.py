import subprocess

def do_ipconfig(self, args):
    """Display network configuration information."""
    try:
        output = subprocess.check_output(["ipconfig"], shell=True)
        print(output.decode())
    except subprocess.CalledProcessError:
        print("Failed to execute 'ipconfig' command.")