import sys
import os
import time
import requests
import socket


def http_req_func():
    print("-------------------------")
    print("Connecting to web servers")
    print("-------------------------")
    print("Connect to server - 0")
    print("exit - 1")
    http_reg_funt_input_command = int(input())
    if http_reg_funt_input_command == 0:
        print("Enter server url...")
        server_url_http_func_input = input()
        url_to_request = server_url_http_func_input
        response_data = http_request(url_to_request)
        print(response_data)
    elif http_reg_funt_input_command == 1:
        exit()
    else:
        print("Not Found.")
        http_req_func()

def http_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"HTTP Error: {response.status_code}"
    except requests.exceptions.RequestException:
        return "Unable to connect to the server."
    

