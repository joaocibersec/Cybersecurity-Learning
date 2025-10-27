import socket

# Simple Port Scanner
target = input("Enter target IP or hostname: ")

# Ports to scan (you can change these)
ports = [21, 22, 23, 80, 443, 8080]

print(f"\nScanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    s.close()

print("\nScan complete!")
