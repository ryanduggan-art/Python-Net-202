ip_addresses = ["10.77.48.123", "192.55.71.22", "192.168.33.22", "172.18.31.55",
                ".58.27.230.221", "109.22.57.3", ".86.2.45.11", "192.168.10.4",
                "192.168.44.71", "172.204.2.5", "10.2.12.7", "192.202.47.18",
                "172.32.55.1"]
#counter for 10. addresses
count_10 = 0

for ip in ip_addresses:
    if ip.startswith("10."):
        print(ip)
        count_10 += 1
    elif ip.startswith("192.168."):
        print(ip)
    elif ip.startswith("172."):
        parts = ip.split(".")
        # splitting 172 address strings into parts and checking the second octet
        if len(parts) > 1 and parts[1].isdigit() and 16 <= int(parts[1]) <= 31:
            print(ip)
print(f"{count_10} IP addresses begin with 10.")
