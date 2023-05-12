import os
import netifaces

def do_ipconfig(self, arg):
    """Display network configuration information."""
    # Get default gateway
    default_gateway = os.popen("ipconfig | findstr Default").read().split(": ")[-1].strip()

    # Get IPv4 and IPv6 addresses
    ipv4_address = os.popen("ipconfig | findstr IPv4").read().split(": ")[-1].strip()
    ipv6_address = os.popen("ipconfig | findstr IPv6").read().split(": ")[-1].strip()

    # Get public IP address
    public_ip_address = os.popen("curl -s https://api.ipify.org").read().strip()
    
    # Get default gateway
    default_gateway = None
    for iface in netifaces.interfaces():
        try:
            gw = netifaces.gateways()['default'][netifaces.AF_INET][0]
            if iface == netifaces.gateways()['default'][netifaces.AF_INET][1]:
                default_gateway = gw
                break
        except KeyError:
            pass


    # Print the results
    print("IPv4 Address:", ipv4_address)
    print("IPv6 Address:", ipv6_address)
    print("Public IP Address:", public_ip_address)
    print("Default Gateway:", default_gateway)
