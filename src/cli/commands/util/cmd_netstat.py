import psutil

def do_netstat(self, args):
    """Displays a list of active network connections."""
    proto = args.lower()
    if proto not in ["tcp", "udp"]:
        print("Invalid protocol. Please enter either 'tcp' or 'udp'")
        return

    # retrieve connections list and filter based on protocol
    conn_list = psutil.net_connections(kind="inet")
    if not proto:
        conn_list = [conn for conn in conn_list if conn.status == psutil.CONN_ESTABLISHED]
    else:
        conn_list = [conn for conn in conn_list if conn.status == psutil.CONN_ESTABLISHED and (proto in conn.type.lower())]

    # print headers
    print(f"{'Proto':<5} {'Local Address':<25} {'Foreign Address':<25} {'Status':<15}")
    print("-" * 75)

    # print connections list
    for conn in conn_list:
        proto = "tcp" if "tcp" in conn.type.lower() else "udp"
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
        status = conn.status
        print(f"{proto:<5} {laddr:<25} {raddr:<25} {status:<15}")
