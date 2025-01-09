# IP Range Validator

## Description

`validate_ip_ranges` is a Python script designed to validate and extract information about a given IP range. It provides detailed information such as WHOIS data and reverse DNS hostnames for IP addresses. It also includes an option to output only the IPs and their associated hostnames for simplified reporting.

### Features
- Validates IP ranges (e.g., `/24`, `/16`).
- Retrieves WHOIS information for each IP.
- Resolves hostnames via reverse DNS lookup.
- Supports concurrent processing for large IP ranges.
- Optional output mode for hostnames and IPs only.

## Requirements

Ensure you have the following installed:

- Python 3.x
- Required modules:
  - `python-whois`
  - `subprocess` (built-in)
  - `ipaddress` (built-in for Python 3.3+)

To install `python-whois`, run:
```bash
pip install python-whois
```

## Usage

Run the script with the desired IP range as a command-line argument. Optionally, use the `--host-only` flag to output only the hostnames and IPs.

### Examples

1. Full details (WHOIS, hostnames):
```bash
python script.py 192.172.12.0/24
```

2. Hostnames and IPs only:
```bash
python script.py 192.172.12.0/24 --host-only
```

### Output

**Full Details:**
```
Validating IP range: 192.172.12.0/24 (256 addresses)
IP: 192.172.12.1
WHOIS: {...}
Host: example.com
----------------------------------------
...
```

**Hostnames and IPs Only:**
```
IP: 192.172.12.1, Host: example.com
IP: 192.172.12.2, Host: another-example.com
...
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your enhancements or bug fixes.

## License

This project is licensed under the MIT License.

