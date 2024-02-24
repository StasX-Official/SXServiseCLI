
import tqdm
import time
import json
import requests
import json
import subprocess
import os
from tqdm import tqdm
from datetime import datetime
from colorama import init, Fore, Back, Style
import ctypes

def error(error, dep_code):
    main_error(error, dep_code)
    
def main_error(error_sxg, code):
    from datetime import datetime
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    file = open("error_logs.txt", "a")
    error_txt = error_sxg

    if code == 0:
        #SXG OTHER ERROR
        code_sys_erro = "OTHER"
        save_error(file, formatted_time, error_txt, code_sys_erro)
    elif code == 1:
        #SXG FUNCTION ERROR
        code_sys_erro = "FUNCTION"
        save_error(file, formatted_time, error_txt, code_sys_erro)
    elif code == 2:
        #SXG SYSTEM ERROR
        code_sys_erro = "SYSTEM"
        save_error(file, formatted_time, error_txt, code_sys_erro)
    else:
        erro_code_auth = "Invalid department code. Error: 7900"
        code_sys_erro = "ERROR_AUTH"
        save_error(file, formatted_time, erro_code_auth, code_sys_erro)


def save_error(file, time, error, code):
    print(time, "SXG - ", error, code)
    text_to_write = f"{time}", error, code, ".\n"
    auth2v = str(text_to_write)
    file.write(auth2v)
    file.close()

global file
file = open("logs.txt", "a")
#Project developer: StasX
#The project is under development
#App version - v5.2024 + AI V0.10BETA
#Copying the code is prohibited by SX copyright.

def starting():
    print("Cheking files...")
    cheak_tm = 0    
    if cheak_tm < 100:
        for _ in tqdm(range(100)):
            import sys
            import time
            cheak_tm += 20
            time.sleep(0.002)
            import qrcode
            import string
            cheak_tm += 20
            time.sleep(0.002)
            import random
            import requests
            cheak_tm += 20
            time.sleep(0.002)
            import platform
            import subprocess
            cheak_tm += 20
            time.sleep(0.002)
            import http.server
            import socketserver
            cheak_tm += 20
            time.sleep(0.002)
     


sxserviseclilogo = Fore.GREEN + """
 #######  ###  ##  #######  #######  ######   ##  ###  #######  #######  #######           #######   ##      #######
 ##       ###  ##  ##       ##       ##  ##   ##  ###    ###    ##       ##                ##  ###   ##        ###
 #######  ###  ##  #######  ##       ##  ##   ##  ###    ###    #######  ##                ##  ###   ##        ###
      ##   #####        ##  #######  #######  ##  ###    ###         ##  #######           ##       ###        ###
 ###  ##  ##  ###  ###  ##  ###      ### ###  ## ####    ###    ###  ##  ###               ##   ##  ###        ###
 ###  ##  ##  ###  ###  ##  # #      ### ###   #####     ###    ###  ##  # #               ##   ##  ###        ###
 #######  ##  ###  #######  #######  ### ###    ###    #######  #######  #######           #######  ######   #######
"""
def start_all(app_name0, version0, app_id0, com0, author0, description0, license0, api_enabled0, api_path0, logs_enabled0, ai_support0, local_default_port0, local_hosting_support0, local_default_path0):
    
    init(autoreset=True)
    ModuleNotFoundError = "Plugin not found. Install the plugin on our website https://sxcomp.42web.io/ or contact SX technical support."
    global current_time
    current_time = datetime.now()
    global formatted_time
    formatted_time = current_time.strftime("%H:%M:%S")
    icon_path = os.path.abspath("logo.ico")
    
    global local_default_port
    local_default_port = local_default_port0
    global local_hosting_support
    local_hosting_support = local_hosting_support0
    global local_default_path
    local_default_path = local_default_path0
    
    global ai_support
    ai_support=ai_support0
    app_name = app_name0
    version = version0
    global app_id
    app_id = app_id0
    global com
    com = com0
    global author
    author = author0
    global description
    description = description0
    global license
    license = license0
    global api_enabled
    api_enabled = api_enabled0
    global api_path
    api_path = api_path0
    global logs_enabled
    logs_enabled = logs_enabled0

    
    global my_app_id
    my_app_id = app_id
    global app_com
    app_com=com
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_com)    

    global app_ver
    app_ver=version
    global app_ai_ver
    app_ai_ver = "AI V0.10BETA"
    global logs1
    logs1=logs_enabled
    starting()
    print(sxserviseclilogo)
    print("Welcome to SXSERVISE CLI 2024!")
    print("Login to your account - login")
    print(" ")
    input_command()


command0 = "exit"
command1 = "help"
command2 = "loginCL"
command3 = "support"
command4 = "localhost"
command5 = "json"
command6 = "qr"
command7 = "qrcode"
command8 = "ping"
command9 = "passworld"
command10 = "sxg install"
command11 = "http"
command12 = "https"
command13 = "dns"
command14 = "host"
command15 = "arduino"
command16 = "ai"
command17="sxscinf"

def command_sxscinf():
    print("SXServiseCLI Info:")
    print("Global info: ")
    print(" /=/Author: ", author)
    print(" /=/Version: ", app_ver)
    print(" /=/Com: ", com)
    print(" /=/Id: ", app_id)
    print("Machine learning:")
    print(" /=/AI Support: ", ai_support)
    print(" /=/AI Version: ", app_ai_ver)
    print("API:")
    print(" /=/API Support: ", api_enabled)
    print(" /=/API Path: ", api_path)
    print("Local Host:")
    print(" /=/default_port:", local_default_port)
    print(" /=/local hosting support: ", local_hosting_support)
    print(" /=/Default path: ", local_default_path)
    input_command()
    
def command_help():
    print("Command list:")
    print("/*/ help - Display this list of commands")
    print("/*/ login - Login to your account BETA")
    print("/*/ support - Contact technical support")
    print("/*/ localhost - Manage local server")
    print("/*/ json - Manage JSON files")
    print("/*/ qrcode - Manage QR codes")
    print("/*/ exit - Exit the program")
    print("/*/ http - Connecting to web servers")
    print("/*/ dns - DNS analysis")
    print("/*/ host - Checking the availability of hosts")
    print("/*/ sxscinf - Application information")
    print("==========================================")
    print("App info:")
    print("SXServiseCLI Version: ", app_ver)
    print("AI Version: ", app_ai_ver)
    print("==========================================")
    print("Difficult commands:")
    print(" ")

    input_command()

def command_support():
    print("Beta version of the application")
    print("If you need assistance or have any questions, please contact our technical support.")
    print("Site - http://sxcomp.42web.io/")
    print("Mail - stasx@engineer.com")
    input_command()

def ping_host(host):
    try:
        subprocess.run(["ping", "-c", "4", host])
        host_to_ping = input("Enter the host to ping: ")
        ping_host(host_to_ping)
    except Exception as e:
        print("Error:", e)
        error("Error code: 4010. Error ping function", 1)

def command_loginCL():
    print("Auth...")
    print("Sign in - 0")
    print("Register - 1")
    user_command_input = int(input(">>> "))
    if user_command_input == 0:
        login_CL_sxg()
    elif user_command_input == 1:
        register_ac_sxg() 
    else:
        print("Error!")
        input_command()
    input_command()

def login_CL_sxg():
    email = input("Enter you mail... >>> ")
    password = input("Enter you password... >>> ")
    url = "https://sxservise.web.app/api/sxservise-cli/auth"

    data = {
        "mail": email,
        "password": password
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Успішний вхід")
        global User
        user = email
    else:
        print("Помилка входу:", response.text)
        
def register_ac_sxg():
    import webbrowser
    url = "https://sxservise.web.app"
    webbrowser.open(url)
    input_command()

def select_ip():
    print("Select IP Address:")
    print("1. Localhost (127.0.0.1)")
    print("2. Custom IP")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        return "127.0.0.1"
    elif choice == "2":
        custom_ip = input("Enter custom IP: ")
        return custom_ip
    else:
        return "Unknown IP"

def additional_information():
    print("Additional Information:")
    print("Enter any additional information you want to store:")
    info = input()
    return info

def command_create_json():
    filename = input("Enter the filename for JSON: ")
    
    data = {}
    print("Enter data for JSON:")
    for key in ["name", "age", "city"]:
        data[key] = input(f"{key.capitalize()}: ")

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(Fore.GREEN + "JSON file created successfully." + Style.RESET_ALL)

def command_read_json():
    filename = input("Enter the filename for JSON: ")
    
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
            print("Data in JSON file:")
            print(data)
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)
        error("Error code: 404. File not found", 1)

def command_check_json_validity():
    filename = input("Enter the filename for JSON: ")
    
    try:
        with open(filename, "r") as json_file:
            json.load(json_file)
            print(Fore.GREEN + "JSON file is valid." + Style.RESET_ALL)
    except json.JSONDecodeError:
        print(Fore.RED + "JSON file is not valid." + Style.RESET_ALL)
        error("Error code: 4041. JSON file is not valid.", 1)

def command_sort_json_data():
    filename = input("Enter the filename for JSON: ")
    
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
            sorted_data = {k: v for k, v in sorted(data.items())}
            print("Sorted JSON data:")
            print(sorted_data)
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)
        error("Error code: 404. File not found", 1)

def command_json_menu():
    print("-----------------")
    print("----json-menu----")
    print("-----------------")
    print("Create json - 0")
    print("Read json - 1")
    print("Check JSON validity - 2")
    print("Sort JSON data - 3")
    print("Exit - 4")

    jsonmenucommand = int(input())
    formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if jsonmenucommand == 0:
        text_to_write = f"{formatted_time} The create_json command is running\n"
        file.write(text_to_write)
        command_create_json()
    elif jsonmenucommand == 1:
        text_to_write = f"{formatted_time} The read_json command is running\n"
        file.write(text_to_write)
        command_read_json()
    elif jsonmenucommand == 2:
        text_to_write = f"{formatted_time} The check_json_validity command is running\n"
        file.write(text_to_write)
        command_check_json_validity()
    elif jsonmenucommand == 3:
        text_to_write = f"{formatted_time} The sort_json_data command is running\n"
        file.write(text_to_write)
        command_sort_json_data()
    elif jsonmenucommand == 4:
        text_to_write = f"{formatted_time} The exit command is running\n"
        file.write(text_to_write)
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        command_json_menu()

def command_additional_info():
    additional_info = additional_information()
    print("Information stored:", additional_info)
    input_command()
import http

def start_lchost_func_sxg():
    if local_hosting_support == True:
        command_localhost()
    elif local_hosting_support == False:
        print("Sorry, but local hosting support is unavailable.")
        error("Error code: 403. Support is unavailable", 1)
        input_command()
    else:
        print("Error reading information from the SXG system file")
        error("Error code: 404. Error reading", 1)
        input_command()


def command_localhost():
    print("")
    print("Start localhost - 0")
    print("Stop localhost - 1")
    print("exit - 2") # taskkill /PID 8000
    print("")
    localhostcommand = int(input(Fore.BLUE + "sxservise >>> "))
    if localhostcommand == 0:
        print("Edit localhost setings: ")
        print("Local host port, default=",local_default_port,":  ")
        local_host_port = int(input())
        print("Local host directory, default=",local_default_path,": ")
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

import socketserver

def start_local_server(port, dir):
    port = port
    directory = dir
    handler = http.server.SimpleHTTPRequestHandler
    handler.directory = directory
    with socketserver.TCPServer(("", port), handler) as httpd:
        message = f"Server started at port {port} - http://localhost:{port}/System/LocalHostData/"
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

def install_package(package_name):
    print(">install package...")
    print("plugin - 0")
    print("package - 1")
    command_install_pcg = int(input(Fore.BLUE + ">>> "))
    if command_install_pcg == 0:
        0
    elif command_install_pcg == 1:
        0
    else:
        print(Fore.RED + "Unknown command.")
        error("Error code: 404. Unknown command", 1)
        install_package()

def input_command():
    global file
    global logs1
    command = input(Fore.BLUE + ">>> ")
    if command == command1:
        text_to_write = f"{formatted_time} The help command is running\n"
        file.write(text_to_write)
        command_help()
    elif command == command2:
        text_to_write = f"{formatted_time} The login command is running\n"
        file.write(text_to_write)
        command_loginCL()
    elif command == "login":
        text_to_write = f"{formatted_time} The login command is running\n"
        file.write(text_to_write)
        command_loginCL()
    elif command == command0:
        text_to_write = f"{formatted_time} The exit command is running\n"
        file.write(text_to_write)
        file.close()
        exit()
    elif command == command3:
        text_to_write = f"{formatted_time} The support command is running\n"
        file.write(text_to_write)
        command_support()
    elif command == command4:
        text_to_write = f"{formatted_time} The localhost command is running\n"
        file.write(text_to_write)
        start_lchost_func_sxg()
    elif command == command5:
        text_to_write = f"{formatted_time} The json command is running\n"
        file.write(text_to_write)
        command_json_menu()
    elif command == command6:
        text_to_write = f"{formatted_time} The qrcode command is running\n"
        file.write(text_to_write)
        from Local.func.qrcodefunc import command_qrcode_menu
    elif command == command7:
        text_to_write = f"{formatted_time} The qrcode command is running\n"
        file.write(text_to_write)
        from Local.func.qrcodefunc import command_qrcode_menu
    elif command == command8:
        text_to_write = f"{formatted_time} The ping command is running\n"
        file.write(text_to_write)
        host_to_ping = input("Enter the host to ping: ")
        ping_host(host_to_ping)
    elif command.startswith("sxg install"):
        text_to_write = f"{formatted_time} The sxg install command is running\n"
        file.write(text_to_write)
        package_name = command[len("sxg install "):]
        install_package(package_name)
    elif command == command11:
        text_to_write = f"{formatted_time} The http command is running\n"
        file.write(text_to_write)
        from Local.func.httpfunc import http_req_func
    elif command == command12:
        text_to_write = f"{formatted_time} The https command is running\n"
        file.write(text_to_write)
        from Local.func.httpfunc import http_req_func
    elif command == command13:
        text_to_write = f"{formatted_time} The dns command is running\n"
        file.write(text_to_write)
        from Local.func.dnsfunc import dns_lookup_func
    elif command == command14:
        text_to_write = f"{formatted_time} The host command is running\n"
        file.write(text_to_write)
        from Local.func.hostav import check_host_av_func
    elif command == command15:
        text_to_write = f"{formatted_time} The arduino command is running\n"
        file.write(text_to_write)
        print("Arduino module is not available in this version.")
        input_command()
    elif command == command16:
        text_to_write = f"{formatted_time} The ai command is running\n"
        file.write(text_to_write)
        from Local.AI.aicommandfunc import aifuncc
        aifuncc()
    elif command == command17:
        text_to_write = f"{formatted_time} The -SXServiseCLI Info- command is running\n"
        file.write(text_to_write)
        command_sxscinf()
    else:
        print(Fore.RED + "Unknown command.")
        error("Error code: 404. Unknown command", 1)
        text_to_write = f"{formatted_time}" + command + "Unknown command.\n"
        file.write(text_to_write)
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        input_command()
