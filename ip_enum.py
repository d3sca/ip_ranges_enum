import ipaddress
import subprocess
import whois
from concurrent.futures import ThreadPoolExecutor

def get_whois_info(ip):
    """Retrieve WHOIS information for a single IP address."""
    try:
        return whois.whois(ip)
    except Exception as e:
        return str(e)

def resolve_host(ip):
    """Perform a reverse DNS lookup to resolve the host name for an IP."""
    try:
        result = subprocess.run(["dig", "-x", ip, "+short"], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

def validate_ip_range(ip_range, host_only=False):
    """Validate and fetch information for all IPs in a given range."""
    try:
        network = ipaddress.ip_network(ip_range, strict=False)
    except ValueError as e:
        print(f"Invalid IP range: {ip_range}")
        return

    print(f"Validating IP range: {ip_range} ({network.num_addresses} addresses)")

    def process_ip(ip):
        ip_str = str(ip)
        whois_info = get_whois_info(ip_str)
        host_info = resolve_host(ip_str)
        return ip_str, whois_info, host_info

    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(process_ip, network))

    for ip, whois_info, host_info in results:
        if host_only:
            print(f"IP: {ip}, Host: {host_info}")
        else:
            print(f"IP: {ip}\nWHOIS: {whois_info}\nHost: {host_info}\n{'-'*40}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py <IP_RANGE> [--host-only]")
        sys.exit(1)

    ip_range = sys.argv[1]
    host_only = len(sys.argv) == 3 and sys.argv[2] == "--host-only"
    validate_ip_range(ip_range, host_only)
