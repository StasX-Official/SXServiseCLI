
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
import qrcode
import socketserver
import socket

current_timeQ12F = datetime.now()
formatted_timeQ12F = current_timeQ12F.strftime("%H:%M:%S")
fileQ12F = open("logs.txt", "a")

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

#Project developer: Kozosvyst Stas (StasX)
#Devoper info: FullName: Kozosvyst Stas; Mail: stasx.official.xx@gmail.com; Google Dev Prof: https://g.dev/StasX; LinkedIn: https://www.linkedin.com/in/stas-kozosvyst-a73782279/ ;
#The project is under development (BETA)
#Copying the code is prohibited by SX copyright.
#GitHub wiki page -> https://github.com/StasX-Official/SXServiseCLI/wiki
#GitHub project page -> https://github.com/StasX-Official/SXServiseCLI
#Thanks a lot for installing! - StasX.

def starting():
    print("Cheking files...")
    cheak_tm = 0    
    if cheak_tm < 100:
        for _ in tqdm(range(100)):
            import sys
            import time
            cheak_tm += 20
            time.sleep(0.02)
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
def start_all(user1mail, user1name, sxservisecliPLUSuser0, app_name0, version0, app_id0, com0, author0, description0, license0, api_enabled0, api_path0, logs_enabled0, ai_support0, local_default_port0, local_hosting_support0, local_default_path0, root_name0, root_pass0):
    
    
    init(autoreset=True)
    from System.Local.sxg.core import core_main
    print("STARTING CORS...")
    core_main(1,0)
    ModuleNotFoundError = "Plugin not found. Install the plugin on our website https://sxcomp.42web.io/ or contact SX technical support."
    global current_time
    current_time = datetime.now()
    global formatted_time
    formatted_time = current_time.strftime("%H:%M:%S")
    icon_path = os.path.abspath("logo.ico")
    
    global username
    username=user1name
    global usermail
    usermail=user1mail
    global sxservisecliPLUS
    sxservisecliPLUS = sxservisecliPLUSuser0
    
    global local_default_port
    local_default_port = local_default_port0
    global local_hosting_support
    local_hosting_support = local_hosting_support0
    global local_default_path
    local_default_path = local_default_path0
    

    global root_name
    root_name=root_name0
    global root_pass
    root_pass=root_pass0
    
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
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(com)    

    global app_ver
    app_ver=version
    global app_ai_ver
    app_ai_ver = "AI V0.10BETA"
    global logs1
    logs1=logs_enabled
    starting()
    
    #CORS STARTING
    
    
    print(sxserviseclilogo)
    print("Welcome to SXSERVISE CLI 2024!")
    print("Login to your account - login")
    print("My tariff plan - plan")
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
command17 = "sxscinf"
command18 = "root"
command19 = "core"
command20 = "control"
command21 = "plan"

def sxservisecliTRPLAN():
    print(" --> User card: ")
    print(" - Auth:")
    print(">UserName - "+username)
    print(">UserMail - "+usermail)
    print(" ")
    print(" --> Plan: ")
    print("SXServiseCLI+ -> "+str(sxservisecliPLUS))
    input_command()

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
        input_command()
    elif http_reg_funt_input_command == 1:
        input_command()
    else:
        print("Not Found.")
        input_command()

def http_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"HTTP Error: {response.status_code}"
    except requests.exceptions.RequestException:
        return "Unable to connect to the server."

def control_command():
    time.sleep(0.5)
    print("-> SXServiseCLI 2024")
    print("Control panel: ")
    print("Sorry, this ALFA command. This command will be available in the official release.")
    input_command()
    
def core_command1():
    print("-----=> SXServiseCLI Core MENU")
    print("Continue - 1")
    print("Exit - 0")
    
    def core_status():
        from System.Local.sxg.core import core_main
        
        servisecore_st = str(core_main(3,0))
    
        print("-----=> SXServiseCLI Core STATUS")
        print("CORE:    STATUS: ")
        print("Servise_CR - "+ servisecore_st)
        print("Auth_CR - ")
        print("LocalHost_CR - ")
        print(" - - - - - - - - - - - - - - -")
        print("True - STARTED, False - Stoped")
    
    def core_menu():
        print(" ")
        print("-SXSERVISECLI CORE MENU-")
        print(" ")
        print("/*/Settings - 2")
        print("/*/Status - 1")
        print("/*/Exit - 0")
        print(" ")
        def core_menu_c_auth(command):
            if command==0:
                input_command()
            elif command == 1 :
                core_status()
            else:
                print("ERROR. 404  Command Not Found.")
                core_menu_c()
                
        def core_menu_c():
            core_menu_inp=int(input(">>> "))
            core_menu_c_auth(core_menu_inp)
            
        core_menu_c()
        
    def core_root_command_inp():
        print("Core - SXServiseCLI2024")
        print(" ")
        print("-=> You will need root access to use it")
        print(" ")
        print("Continue - 0")
        print("Exit - 1")
        print(" ")
        
        def core_root_command_inp_command_auth(command0or1):
            def core_root_command_error(error):
                print("ERROR! ", error)
                print("Restart? ")
                print(" ")
                print("Continue - 1")
                print("Exit - 0")
                print(" ")
                
                def core_root_command_error_input_auth(command):
                    if command==1:
                        core_root_command_inp()
                    elif command==0:
                        input_command()
                    else:
                        print("ERROR! Invalid Input")
                        core_root_command_error_input()
                    
                def core_root_command_error_input():
                    core_root_command_error_input_command=str(input(">>> "))
                    core_root_command_error_input_auth(core_root_command_error_input_command)
                    
                core_root_command_error_input()
            if command0or1==0:
                def root_pass_core_command_check(root_name9,root_pass9):
                    time.sleep(1)
                    if logs_enabled==True:
                        print("Logs enabled!")
                        if root_name9==root_name:
                            print("AUTH_LOGS: ROOT_NAME AUTH TRUE!")
                            time.sleep(1)
                            if root_pass9==root_pass:
                                print("AUTH_LOGS: ROOT_PASS AUTH TRUE!")
                                core_menu()
                            else:
                                print("AUTH_LOGS: ROOT_PASS AUTH FALSE!")
                                core_root_command_error("ROOT PASSWORD WRONG")
                        else:
                            print("AUTH_LOGS: ROOT_NAME AUTH FALSE!")
                            core_root_command_error("ROOT NAME WRONG")

                
                print(" ")
                print("Enter ROOT_NAME...")
                core_auth1_root_name=str(input(">>> "))
                print("Enter ROOT_PASS...")
                core_auth1_root_pass=str(input(">>> "))
                root_pass_core_command_check(core_auth1_root_name, core_auth1_root_pass)
            elif command0or1==1:
                input_command()
            else:
                print("ERROR. 404. Command not found.")
                print("0 - Continue, 1 - Exit... Enter 0 or 1...")
                core_root_command_inp_command()

        def core_root_command_inp_command():
            core_root_command_inp_c=int(input(">>> "))
            core_root_command_inp_command_auth(core_root_command_inp_c)
            
        core_root_command_inp_command()
    
    def auth_core_command_inp_auth(command0or1):
        if command0or1==0:
            input_command()
        elif command0or1==1:
            core_root_command_inp()
        else:
            print("ERROR. 404")
            auth_core_command_inp()
    
    def auth_core_command_inp():
        start_core_command_inp=int(input(">>> "))
        auth_core_command_inp_auth(start_core_command_inp)
    
    auth_core_command_inp()


def host_command():
    print("Host - SXServiseCLI2024")
    print(" ")
    print("-=> You will need root access to use it")
    print(" ")
    print("Continue - 0")
    print("Exit - 1")
    print(" ")
    def auth():
        continue_command=int(input(">>> "))
        if continue_command==1:
            input_command()
        elif continue_command==0:
            def root_auth1():
                print("Enter ROOT_NAME")
                root_name0=input(">>> ")
                print("Enter ROOT_PASS")
                root_pass0=input(">>> ")
                host_root_auth_main(root_name0,root_pass0)
            root_auth1()
        else:
            print("Error! 404. Invalid Num")
            auth(">>> ")
    
    def host_root_auth_main(rootname,rootpass):
        #logic
        if rootname==root_name:
            if logs_enabled==True:
                print("AUTH-LOG: ROOT_NAME Valid")
                time.sleep(1)
                if  rootpass==root_pass:
                    print("AUTH-LOG: ROOT_PASS Valid")
                    if local_hosting_support==True:
                        check_host_av_func()
                    else:
                        print("Host support - OFF")
                        input_command()
                else:
                    print("AUTH-LOG: ROOT_PASS Invalid")
                    q1ex="ROOT_PASS"
                    error_lc_3(q1ex)
                    
            time.sleep(1)
            if  rootpass==root_pass:
                start_lchost_func_sxg()
            else:
                q1ex="ROOT_PASS"
                error_lc_3(q1ex)

        elif rootpass==root_pass:
            if logs_enabled==True:
                print("AUTH-LOG: ROOT_NAME Invalid")
                time.sleep(1)
                print("AUTH-LOG: ROOT_PASS Valid")
                q2ex1="ROOT_NAME"
                error_lc_3(q2ex1)
            
            time.sleep(1)
            q2ex1="ROOT_NAME"
            error_lc_3(q2ex1)
                
        else:
            def error_lc_3(errorc):
                print("ERROR: Incorrect information. ", errorc)
                print("-=> Please try again")
                print(" ")
                print("Try again - 1")
                print("Exit - 0")
                print(" ")
                global host_auth_main_truagain
                host_auth_main_truagain=int(input(">>> "))
                if host_auth_main_truagain==0:
                    input_command()
                elif host_auth_main_truagain==1:
                    input_command()
                else:
                    print("Errot!  Wrong number")
                    input_command()
    auth()
            
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
            input_command()
        else:
            print(f"{host}:{port} is not reachable.")
            input_command()

    elif check_host_availability_command_input == 1:
        input_command()
    else:
        print("Not Found.")
        check_host_av_func()


def check_host_availability(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        return True
    except (socket.timeout, ConnectionError):
        return False
    


def create_qrcode():
    print("Your text for the QR code:")
    qrcodetextdata = input()
    qrcodesizedataY = int(input("QR code cell size (default is 10): "))
    qrcodesizedataX = int(input("Border width (default is 4): "))
    
    print("Creating your QR code...")
    time.sleep(1)
    
    data = qrcodetextdata
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=qrcodesizedataY,
        border=qrcodesizedataX,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = "qrcode.png"
    img.save(img_path)
    
    print("QR code created successfully!")
    os.startfile(img_path)
    input_command()

def command_qrcode_menu1():
    print("-----------")
    print(" -> QR-Code")
    print("-----------")
    print("/*/- Create - 0")
    print("/*/-Edit Existing - 1")
    print("/*/-Decode - 2")
    print("/*/-Wi-Fi QR Code - 3")
    print("/*/-Exit   - 4")
    print("-----------")
    command_qrcode23 = int(input(Fore.BLUE + ">>> "))
    
    if command_qrcode23 == 0:
        create_qrcode()
    elif command_qrcode23 == 1:
        edit_qrcode()
    elif command_qrcode23 == 2:
        decode_qrcode()
    elif command_qrcode23 == 3:
        create_wifi_qrcode()
    elif command_qrcode23 == 4:
        text_to_write = f"{formatted_timeQ12F} The exit command is running\n"
        file.write(text_to_write)
        input_command()
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_timeQ12F} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        command_qrcode_menu1()

    
def edit_qrcode():
    filename = input("Enter the filename of the QR code to edit: ")
    
    try:
        with open(filename, "r") as qr_file:
            qrcodetextdata = qr_file.readline().strip()
        print("Editing QR code:", qrcodetextdata)
        
        new_text = input("Enter new text for the QR code: ")
        
        with open(filename, "w") as qr_file:
            qr_file.write(new_text)
        print("QR code updated successfully!")
        input_command()
        
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)
        input_command()

def decode_qrcode():
    print("Decode QR code:")
    qrcode_image = input("Enter the filename of the QR code image: ")
    
    try:
        img = qrcode.make(qrcode_image)
        qr_data = img.data.decode("utf-8")
        print("Decoded data:", qr_data)
        input_command()
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)
        input_command()
    except UnicodeDecodeError:
        print(Fore.RED + "Error decoding QR code." + Style.RESET_ALL)
        input_command()

def create_wifi_qrcode():
    ssid = input("Enter Wi-Fi SSID: ")
    password = input("Enter Wi-Fi Password: ")
    
    wifi_qr_data = f"WIFI:S:{ssid};T:WPA;P:{password};;"
    qrcodesizedataY = int(input("QR code cell size (default is 10): "))
    qrcodesizedataX = int(input("Border width (default is 4): "))
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=qrcodesizedataY,
        border=qrcodesizedataX,
    )
    qr.add_data(wifi_qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = "wifi_qrcode.png"
    img.save(img_path)
    
    print("Wi-Fi QR code created successfully!")
    os.startfile(img_path)
    input_command()
    
def root_menu():
    print("Root Munu: ")
    print("Root info - 1")
    print("Exit - 0")
    rootcommand=int(input(">>> "))
    if rootcommand==1:
        print(" ")
        print("Root info...")
        print("Show root information?  y/n")
        def show_root_info():
            print(" ")
            q1=str(input(">>> "))
            if q1=="y":
                print("  SXSERVISECLI ROOT INFO:")
                time.sleep(2)
                print("/*/ - Root name - ", root_name, "SYSTEM: sxservisecli1")
                print("/*/ - Root pass - ", root_pass, "SYSTEM: sxservisecli1")
                print(" ")
                input_command()
            elif q1=="n":
                input_command()
            else:
                show_root_info()
        show_root_info()         
    elif  rootcommand==0:
        input_command()

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
    print("/*/ localhost - Manage local server (BETA)")
    print("/*/ json - Manage JSON files")
    print("/*/ qrcode - Manage QR codes")
    print("/*/ exit - Exit the program")
    print("/*/ http - Connecting to web servers")
    print("/*/ dns - DNS analysis (BETA)")
    print("/*/ host - Checking the availability of hosts")
    print("/*/ sxscinf - Application information")
    print("/*/ root - SXServiseCLI Root (BETA)")
    print("/*/ core - SXServiseCLI Core Menu (BETA)")
    print("==========================================")
    print("App info:")
    print("SXServiseCLI Version: ", app_ver)
    print("AI Version: ", app_ai_ver)
    print("==========================================")
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
    print("LocalHost - SXServiseCLI2024")
    print(" ")
    print("-=> You will need root access to use it")
    print(" ")
    print("Continue - 0")
    print("Exit - 1")
    print(" ")
    def localhost_root_auth_main(rootname,rootpass):
        #logic
        if rootname==root_name:
            if logs_enabled==True:
                print("AUTH-LOG: ROOT_NAME Valid")
                time.sleep(1)
                if  rootpass==root_pass:
                    print("AUTH-LOG: ROOT_PASS Valid")
                    if local_hosting_support==True:
                        localhost_menu()
                    else:
                        print("Local Host support - OFF")
                        input_command()
                else:
                    print("AUTH-LOG: ROOT_PASS Invalid")
                    q1ex="ROOT_PASS"
                    error_lc_3(q1ex)
                    
            time.sleep(1)
            if  rootpass==root_pass:
                start_lchost_func_sxg()
            else:
                q1ex="ROOT_PASS"
                error_lc_3(q1ex)

        elif rootpass==root_pass:
            if logs_enabled==True:
                print("AUTH-LOG: ROOT_NAME Invalid")
                time.sleep(1)
                print("AUTH-LOG: ROOT_PASS Valid")
                q2ex1="ROOT_NAME"
                error_lc_3(q2ex1)
            
            time.sleep(1)
            q2ex1="ROOT_NAME"
            error_lc_3(q2ex1)
                
        else:
            def error_lc_3(errorc):
                print("ERROR: Incorrect information. ", errorc)
                print("-=> Please try again")
                print(" ")
                print("Try again - 1")
                print("Exit - 0")
                print(" ")
                global localhost_auth_main_truagain
                localhost_auth_main_truagain=int(input(">>> "))
                localhost_auth_main_truagain_auth()
                
            def localhost_auth_main_truagain_auth():
                if localhost_auth_main_truagain==1:
                    command_localhost()
                elif localhost_auth_main_truagain==0:
                    input_command()
                else:
                    print("ERROR: Incorrect information. Please try again")
                    print(" ")

            rert="ROOT_NAME, ROOT_PASS"
            error_lc_3(rert)
                    
                    
    def localhost_root_auth():
        r1=int(input(">>> "))
        if r1==0:
            print(" ")
            print("Enter the root name...")
            localhost_root_auth_name=str(input(">>> "))
            print("Enter the root pass...")
            localhost_root_auth_pass=str(input(">>> "))
            print("Auth...")
            localhost_root_auth_main(localhost_root_auth_name, localhost_root_auth_pass)
        elif r1==1:
            input_command()
        else:
            print("Error. Enter a numeric value (0-1)")
            localhost_root_auth()
    localhost_root_auth()
        
def localhost_menu():
    print("")
    print("====================")
    print("=====LocalHost======")
    print("====================")
    print("Start localhost - 0")
    print("Stop localhost - 1")
    print("exit - 2") # taskkill /PID 8000
    print("====================")
    print("# taskkill /PID 8000")
    print("====================")
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
        pass
    elif command_install_pcg == 1:
        pass
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
        command_localhost()
    elif command == command5:
        text_to_write = f"{formatted_time} The json command is running\n"
        file.write(text_to_write)
        command_json_menu()
    elif command == command6:
        text_to_write = f"{formatted_time} The qrcode command is running\n"
        file.write(text_to_write)
        command_qrcode_menu1()
    elif command == command7:
        text_to_write = f"{formatted_time} The qrcode command is running\n"
        file.write(text_to_write)
        command_qrcode_menu1()
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
        http_req_func()
    elif command == command12:
        text_to_write = f"{formatted_time} The https command is running\n"
        file.write(text_to_write)
        http_req_func()
    elif command == command13:
        text_to_write = f"{formatted_time} The dns command is running\n"
        file.write(text_to_write)
        check_host_av_func()
    elif command == command14:
        text_to_write = f"{formatted_time} The host command is running\n"
        file.write(text_to_write)
        host_command()
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
    elif command == "root":
        text_to_write = f"{formatted_time} The -SXServiseCLI Root- command is running\n"
        file.write(text_to_write)
        root_menu()  
    elif command == command19:
        text_to_write = f"{formatted_time} The -SXServiseCLI CORE- command is running\n"
        file.write(text_to_write)
        core_command1()
    elif command==command20:
        text_to_write = f"{formatted_time} The CONTROL command is running\n"
        file.write(text_to_write)
        control_command()
    elif command==command21:
        text_to_write = f"{formatted_time} The PLAN command is running\n"
        file.write(text_to_write)
        sxservisecliTRPLAN()
    else:
        print(Fore.RED + "Unknown command.")
        error("Error code: 404. Unknown command", 1)
        text_to_write = f"{formatted_time}" + command + "Unknown command.\n"
        file.write(text_to_write)
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        input_command()
    
