import re


def is_valid_ip_port(ip_port: str) -> bool:
    pattern: str = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]+$"
    match = re.match(pattern, ip_port)

    if not match:
        return False

    ip, port = ip_port.split(":")
    port = int(port)

    ip_segments = ip.split(".")
    if all(0 <= int(segment) <= 255 for segment in ip_segments) and (
        0 <= port <= 65535
    ):
        return True

    return False
