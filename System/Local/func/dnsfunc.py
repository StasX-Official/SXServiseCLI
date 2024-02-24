import sys
import os
import time
import requests
import socket

def dns_lookup_func():
    print("-------------------------")
    print("      DNS analysis")
    print("-------------------------")
    print("Run the check - 0")
    print("exit - 1")

    dns_lookup_func_input_command = int(input())

    if dns_lookup_func_input_command == 0:
        print("Enter the domain...")
        dns_lookup_func_input_command_domain = input()
        domain_to_lookup = dns_lookup_func_input_command_domain
        result = dns_lookup(domain_to_lookup)
        print(result)
    elif dns_lookup_func_input_command == 1:
        exit()
    else:
        print("Not Found")
        dns_lookup_func()

  
def dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return f"Domain: {domain}, IP Address: {ip_address}"
    except socket.gaierror:
        return f"Domain {domain} not found."