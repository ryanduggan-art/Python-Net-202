from scapy.all import ARP, Ether, srp, conf
import ipaddress

def get_local_cidr():
    # Correct tuple order: (iface_name, local_ip, gateway_ip)
    iface, local_ip, gw = conf.route.route("0.0.0.0")

    # Try to get the netmask from Scapy's iface table
    # On some OSes this may be None; if so, fall back to /24
    nm = None
    try:
        nm = conf.ifaces[iface].netmask
    except Exception:
        nm = None

    if not nm:
        # Sensible fallback if Scapy doesn't expose netmask
        return f"{local_ip}/24", iface

    network = ipaddress.IPv4Network(f"{local_ip}/{nm}", strict=False)
    return str(network), iface

def scan_network_auto(timeout=3):
    cidr, iface = get_local_cidr()
    print(f"Scanning {cidr} on interface {iface}")
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=cidr)
    answered, _ = srp(pkt, timeout=timeout, verbose=0, iface=iface)
    devices = []
    for _, r in answered:
        devices.append({'ip': r.psrc, 'mac': r.hwsrc})
    return devices

if __name__ == "__main__":
    devices = scan_network_auto()
    if not devices:
        print("No hosts responded.")
    else:
        for d in devices:
            print(f"IP: {d['ip']:<15} MAC: {d['mac']}")
