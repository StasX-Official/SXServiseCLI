import sys
import time
import os
import json
import tqdm
import qrcode
import string
import ctypes
import random
import platform
import subprocess
import http.server
import socketserver
from tqdm import tqdm
from datetime import datetime
from colorama import init, Fore, Back, Style

command0 = "exit"

init(autoreset=True)
ModuleNotFoundError = "Plugin not found. Install the plugin on our website https://sxcomp.42web.io/ or contact SX technical support."
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
Yes = True
No = False
file = open("logs.txt", "a")

def command_localhost():
    print("")
    print("Start localhost - 0")
    print("Stop localhost - 1")
    print("exit - 2") # taskkill /PID 8000
    print("")
    localhostcommand = int(input(Fore.BLUE + "sxservise >>> "))
    if localhostcommand == 0:

        print("Edit localhost setings: ")
        print("Local host port, default=8000:  ")
        local_host_port = int(input())
        print("Local host directory, default=localhostData: ")
        local_host_directory = input()

        print("Starting localhost...")
        for i in tqdm(range(100)):
            time.sleep(0.01)
        text_to_write = f"{formatted_time} Starting localhost...\n"
        file.write(text_to_write)

        start_local_server(local_host_port, local_host_directory)

    elif localhostcommand == 1:
        print("Stopping localhost...")
        for i in tqdm(range(100)):
            time.sleep(0.005)
        text_to_write = f"{formatted_time} The stop_localhost command is running\n"
        file.write(text_to_write)
        stop_local_server()
    elif localhostcommand == 2:
        text_to_write = f"{formatted_time} The exit command is running\n"
        file.write(text_to_write)
    elif localhostcommand == command0:
        text_to_write = f"{formatted_time} The exit command is running\n"
        file.write(text_to_write)
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        command_localhost()

def stop_local_server():
    print("Stopping the server.")
    text_to_write = f"{formatted_time} Stopping the localhost server.\n"
    file.write(text_to_write)
    raise KeyboardInterrupt

def start_local_server(port, dir):
    port = port
    directory = dir
    handler = http.server.SimpleHTTPRequestHandler
    handler.directory = directory
    with socketserver.TCPServer(("", port), handler) as httpd:
        message = f"Server started at port {port} - http://localhost:{port}/"
        print(Fore.RED + "Press Control + C to stop localhost")
        print(message)

        message = f"Serving directory: {directory}"
        print(message)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            text_to_write = f"{formatted_time} Localhost server stopped.\n"
            file.write(text_to_write)
            print("Server stopped.")