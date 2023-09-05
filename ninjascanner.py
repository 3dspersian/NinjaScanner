#!/usr/bin/python3

import os
import re
import sys
from colorama import Fore, Style

ASCII_ART = r"""
  ____ _____ _       _____           
 / ___|_   _| |     | ____|__ _ _ __  
| |     | | | |     |  _| / _` | '_ \ 
| |___  | | | |___  | |__| (_| | | | |
 \____| |_| |_____| |_____\__,_|_| |_|
"""
print(ASCII_ART)
if len(sys.argv) != 2 or sys.argv[1] == '-h':
    print("Usage: ./scanner.py <ip_address>")
    sys.exit(1)
else:
    target = sys.argv[1]
# target = input("[+] Enter the Target IP: ")
output_file = "nmap.tmp"
open_ports = []

# Run the Nmap scan and redirect output to a file
print("\nScanning... :D\n")
os.system(f"nmap -p- -T5 {target} >> {output_file}")
print("[-] Scan Complete!\n[+] Parsing through scan to return open ports...")

# Open the output file and read its contents
with open(output_file, 'r') as file:
    for line in file:
        match = re.match(r'^(\d+)/', line.strip())
        if match:
            port_number = match.group(1)
            open_ports.append(port_number)

# Remove the temporary file
os.remove(output_file)

# Print the extracted open ports
print("\nOpen Ports:")
for port in open_ports:
    print(Fore.YELLOW + port + Style.RESET_ALL)

print("\n[+] Now running a deeper scan on the open ports...")
joined_ports = ','.join(open_ports)

os.system(f"nmap -p {joined_ports} -A {target} -oN nmap.scan")

print(f"\n\n [!] Results stored in {Fore.RED}'nmap.scan'{Style.RESET_ALL}")
