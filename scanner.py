import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        print(f"[OPEN] Port {port}")
        s.close()
    except:
        pass

def main(ip, ports):
    print(f"🔍 Scanning {ip}...")
    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in ports:
            executor.submit(scan_port, ip, port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("ip", help="Target IP address to scan")
    parser.add_argument("--start", type=int, default=20, help="Start port")
    parser.add_argument("--end", type=int, default=100, help="End port")
    args = parser.parse_args()

    port_range = range(args.start, args.end + 1)
    main(args.ip, port_range)
