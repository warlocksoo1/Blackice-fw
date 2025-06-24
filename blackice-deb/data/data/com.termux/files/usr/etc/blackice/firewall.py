import argparse
import datetime
import json
import os

from termcolor import colored

RULES_FILE = "rules.json"
LOG_FILE = "firewall.log"

# Fake traffic simulation
fake_traffic = [
    {"ip": "192.168.1.5", "port": 80},
    {"ip": "10.0.0.1", "port": 443},
    {"ip": "192.168.1.9", "port": 21},
    {"ip": "10.10.10.10", "port": 8080},
    {"ip": "8.8.8.8", "port": 80}
]

def load_rules():
    return json.load(open(RULES_FILE)) if os.path.exists(RULES_FILE) else []

def save_rules(rules):
    json.dump(rules, open(RULES_FILE, "w"))

def log_event(ip, port, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {status} IP {ip} on Port {port}\n"
    with open(LOG_FILE, "a") as f:
        f.write(line)

def test_firewall():
    allowed_ports = load_rules()
    for pkt in fake_traffic:
        ip, port = pkt["ip"], pkt["port"]
        if port in allowed_ports:
            status = "[ALLOWED]"
            print(colored(f"{status} IP {ip} on Port {port}", "green"))
        else:
            status = "[BLOCKED]"
            print(colored(f"{status} IP {ip} on Port {port}", "red"))
        log_event(ip, port, status)

def add_port(port):
    rules = load_rules()
    if port not in rules:
        rules.append(port)
        save_rules(rules)
        print(f"[+] Port {port} added to allowed list.")
    else:
        print(f"[!] Port {port} already allowed.")

def remove_port(port):
    rules = load_rules()
    if port in rules:
        rules.remove(port)
        save_rules(rules)
        print(f"[-] Port {port} removed from allowed list.")
    else:
        print(f"[!] Port {port} not found in allowed list.")

def show_ports():
    print("✅ Allowed Ports:", load_rules())

def show_log():
    if os.path.exists(LOG_FILE):
        print("\n".join(open(LOG_FILE).readlines()))
    else:
        print("[!] No log found.")

def clear_log():
    open(LOG_FILE, "w").close()
    print("[✔] Log file cleared.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blackice Firewall Simulator")
    parser.add_argument('--test', action='store_true')
    parser.add_argument('--add-port', type=int)
    parser.add_argument('--remove-port', type=int)
    parser.add_argument('--show-ports', action='store_true')
    parser.add_argument('--show-log', action='store_true')
    parser.add_argument('--clear-log', action='store_true')

    args = parser.parse_args()

    if args.test:
        test_firewall()
    elif args.add_port:
        add_port(args.add_port)
    elif args.remove_port:
        remove_port(args.remove_port)
    elif args.show_ports:
        show_ports()
    elif args.show_log:
        show_log()
    elif args.clear_log:
        clear_log()
    else:
        parser.print_help()
