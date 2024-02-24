import sys
import os
import time
import requests
import socket

def check_host_av_func():
    print("-------------------------")
    print("Host availability review")
    print("-------------------------")
    print("Run the check - 0")
    print("exit - 1")
    check_host_availability_command_input = int(input())
    if check_host_availability_command_input == 0:
        print("Enter host...")
        host = input()
        print("Enter port... Default 80")
        port = int(input())
        if check_host_availability(host, port):
            print(f"{host}:{port} is reachable.")
        else:
            print(f"{host}:{port} is not reachable.")

    elif check_host_availability_command_input == 1:
        exit()
    else:
        print("Not Found.")
        check_host_av_func()


def check_host_availability(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        return True
    except (socket.timeout, ConnectionError):
        return False