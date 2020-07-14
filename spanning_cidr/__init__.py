import ipaddress

__version__ = '0.1.1'


def spanning_cidr(ip_addrs: list) -> str:
    ips = [ipaddress.IPv4Address(ip) for ip in ip_addrs if ip]

    if not ips:
        return

    if len(ips) == 1:
        return str(ipaddress.ip_network(ips[0]))

    lowest_ip, highest_ip = min(ips), max(ips)
    mask_length = ipaddress.IPV4LENGTH - \
        len(bin(int(lowest_ip) ^ int(highest_ip))[2:])
    network_ip = ipaddress.ip_network(
        f'{lowest_ip}/{mask_length}', strict=False)
    return str(network_ip)
