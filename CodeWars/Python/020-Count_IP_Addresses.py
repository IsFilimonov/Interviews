import ipaddress

def ips_between(start, end):
    return int(ipaddress.ip_address(end)) - int(ipaddress.ip_address(start))