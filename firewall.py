# firewall.py
import argparse
import os
import json

# Rule file paths
BLOCKED_IPS_FILE = "blocked_ips.json"
ALLOWED_PORTS_FILE = "allowed_ports.json"

# Load or create rule files
def load_list(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump([], f)
    with open(filename, "r") as f:
        return json.load(f)

def save_list(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

blocked_ips = load_list(BLOCKED_IPS_FILE)
allowed_ports = load_list(ALLOWED_PORTS_FILE)

# Firewall check
def check_packet(ip, port):
    if ip in blocked_ips:
        return f"[BLOCKED] IP {ip} is blacklisted."
    elif port not in allowed_ports:
        return f"[BLOCKED] Port {port} is not allowed."
    else:
        return f"[ALLOWED] IP {ip} on Port {port}."

# CLI options
parser = argparse.ArgumentParser(description="Termux Firewall Control")

parser.add_argument("--add-ip", help="Add IP to block list")
parser.add_argument("--remove-ip", help="Remove IP from block list")
parser.add_argument("--allow-port", type=int, help="Add port to allow list")
parser.add_argument("--remove-port", type=int, help="Remove port from allow list")
parser.add_argument("--test", action="store_true", help="Run test packets")

args = parser.parse_args()

# Handle CLI actions
if args.add_ip:
    if args.add_ip not in blocked_ips:
        blocked_ips.append(args.add_ip)
        save_list(BLOCKED_IPS_FILE, blocked_ips)
        print(f"[+] Blocked IP added: {args.add_ip}")
    else:
        print(f"[!] IP already blocked.")

elif args.remove_ip:
    if args.remove_ip in blocked_ips:
        blocked_ips.remove(args.remove_ip)
        save_list(BLOCKED_IPS_FILE, blocked_ips)
        print(f"[-] Blocked IP removed: {args.remove_ip}")
    else:
        print(f"[!] IP not in block list.")

elif args.allow_port:
    if args.allow_port not in allowed_ports:
        allowed_ports.append(args.allow_port)
        save_list(ALLOWED_PORTS_FILE, allowed_ports)
        print(f"[+] Port allowed: {args.allow_port}")
    else:
        print(f"[!] Port already allowed.")

elif args.remove_port:
    if args.remove_port in allowed_ports:
        allowed_ports.remove(args.remove_port)
        save_list(ALLOWED_PORTS_FILE, allowed_ports)
        print(f"[-] Port removed: {args.remove_port}")
    else:
        print(f"[!] Port not in allow list.")

elif args.test:
    # Run test packet simulation
    test_packets = [
        ("192.168.1.5", 80),
        ("192.168.1.10", 21),
        ("10.0.0.1", 443),
        ("172.16.0.2", 8080),
        ("8.8.8.8", 80),
    ]
    for ip, port in test_packets:
        print(check_packet(ip, port))

else:
    parser.print_help()
