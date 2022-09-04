SELECT id, (last::inet - first::inet) AS ips_between
FROM ip_addresses;