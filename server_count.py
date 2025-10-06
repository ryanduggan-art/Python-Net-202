import pprint

windows_servers = {'management01': '10.10.10.2', 'sccm01': '10.10.10.3',
                   'domaincontroller01': '10.10.10.4', 'domaincontroller02': '10.10.10.5',
                   'sql01': '10.10.10.6', 'exchange01': '10.10.10.7'}

linux_servers = {'applications01': '10.10.20.2', 'ftp01': '10.10.20.3',
                 'vulnscanner01': '10.10.20.4', 'ldap01': '10.10.20.5', 'dns01': '10.10.20.6',
                 'dns02': '10.10.20.7', 'dhcp01': '10.10.20.8'}

# Determine number of Windows and Linux servers
def count_servers(windows, linux):
    # Returns length of Windows and Linux dictionaries
    return len(windows), len(linux)

def add_windows_server(windows, name, ip):
    # Adds a Windows Server
    windows[name] = ip

def get_assigned_ips(windows, linux):
    # Returns list of Windows and Linux dictionary values (IP addresses)
    return (list(windows.values()) + list(linux.values()))

def get_server_names(windows, linux):
    # Returns list of Windows and Linux dictionary keys (Server names)
    return list(windows.keys()) + list(linux.keys())

def main():
    # Totaling and printing server counts
    win_count, lin_count = count_servers(windows_servers, linux_servers)
    print(f"Total Windows Servers: {win_count}")
    print(f"Total Linux Servers: {lin_count}")

    # Adding Barry's Windows Print Server
    add_windows_server(windows_servers, "BarrysPrintSvr", "10.10.10.8")
    print("Updated Windows Servers:")
    pprint.pprint(windows_servers)

    # Printing all assigned IPs (both servers)
    all_ips = get_assigned_ips(windows_servers, linux_servers)
    print("All Assigned IPs:\n", all_ips)

    # Printing server names (both servers)
    names = get_server_names(windows_servers, linux_servers)
    print("Assigned Server Names:\n", names)

if __name__ == '__main__':
    main()