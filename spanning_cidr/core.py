import ipaddress


def spanning_cidr(ip_addrs: list) -> str:
    """
    Function that accepts a sequence of IP addresses 
    returning a single subnet that is large enough to 
    span the lower and upper bound IP addresses with a 
    possible overlap on either end.

    :param ip_addrs: sequence of IP addresses
    :return: a single spanning subnet
    """
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
