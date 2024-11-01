import json
import sys
import os
import time
from ftplib import FTP
from tqdm import tqdm
import random
import paramiko
import os
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from getpass import getpass
import ctypes
from colorama import Fore
from System.media.logo import sxscli_logo_
from System.color_map import color_map
import socket
import whois
import dns.resolver
import ssl
import concurrent.futures
import logging
import platform
import subprocess
from datetime import datetime
from System.cfg_path_map import path_addons_cfg, path_api_cfg, path_system_cfg, path_localhost_cfg, path_user_cfg, path_pers_cfg
from rich.console import Console
from rich.prompt import Prompt
from rich.tree import Tree
from rich import box
import colorama
colorama.init(autoreset=True)

class SXServiseCLI:
    def __init__(self, other):
        
        self.console = Console()
        
        with open(path_addons_cfg, 'r') as cache_ootgg2:
            self.addons_cfg = json.load(cache_ootgg2)
        
        with open(path_api_cfg, 'r') as cache_ootgg2f:
            self.api_cfg = json.load(cache_ootgg2f)
            
        with open(path_system_cfg, 'r') as cache_ootgg2fq:
            self.system_cfg = json.load(cache_ootgg2fq)
        
        with open(path_user_cfg, "r") as cache_rerwfds:
            self.user_cfg = json.load(cache_rerwfds)
        
        with open(path_localhost_cfg, "r") as cache_fdfsfsfsfq:
            self.localhost_cfg = json.load(cache_fdfsfsfsfq)
        
        with open(path_pers_cfg, "r") as cache_gksjnqfqq:
            self.pers_cfg = json.load(cache_gksjnqfqq)

            
        self.logo=sxscli_logo_
        cont_debug_json={
    "debug_status": False,
    "debug_settings": {
        "level_": "INFO",
        "show_debug_message": False,
        "format": "%(asctime)s - %(name)s - %(levelname)s - SXSCLI: %(message)s"
    }
}
        self.staff_path=self.system_cfg["STAFF"]["path"]
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path)
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/logs")
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/results")
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/projects")
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/dlc")
        SXServiseCLI.check_and_create_json(self, self.staff_path+"/debug.json", cont_debug_json)
        with open("Staff\debug.json","r") as cache_fdfdfqqqqq:
            self.debug_cfg = json.load(cache_fdfdfqqqqq)        
        handlers = [logging.FileHandler(self.staff_path + "/logs/cli_logs.log")]
        if self.debug_cfg["debug_status"]:
            if self.debug_cfg["debug_settings"]["show_debug_message"]:
                handlers.append(logging.StreamHandler()) 
        
        if self.debug_cfg["debug_settings"]["level_"] == "DEBUG":
            level = logging.DEBUG
        elif self.debug_cfg["debug_settings"]["level_"] == "INFO":
            level = logging.INFO
        elif self.debug_cfg["debug_settings"]["level_"] == "WARNING":
            level = logging.WARNING
        elif self.debug_cfg["debug_settings"]["level_"] == "ERROR":
            level = logging.ERROR
        elif self.debug_cfg["debug_settings"]["level_"] == "CRITICAL":
            level = logging.CRITICAL
        else:
            level = logging.INFO
        
        
        if self.system_cfg["settings"]["logs"]==True:
            log_dir = os.path.dirname(self.staff_path + "/logs/cli_logs.log")
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            logging.basicConfig(
                level=level,
                format=self.debug_cfg["debug_settings"]["format"],
                handlers=handlers
            )
        else:
            log_dir = os.path.dirname(self.staff_path + "/logs/cli_logs.log")
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            logging.basicConfig(
                level=level,
                format=self.debug_cfg["debug_settings"]["format"]
            )
            
        logging.info("Initialization started.")
        try:
            self.app_name = self.system_cfg["appName"]
            self.app_version = self.system_cfg["version"]
            self.app_id = self.system_cfg["id"]
            self.app_com = self.system_cfg["com"]
            self.author = self.system_cfg["author"]
            self.description = self.system_cfg["description"]
            self.license = self.system_cfg["license"]
            self.settings_api = self.system_cfg["settings"]["api"]
            self.settings_api_path = self.system_cfg["settings"]["api_path"]
            self.settings_AuthAPI = self.system_cfg["settings"]["AuthAPI"]
            self.settings_ServisesAPI = self.system_cfg["settings"]["ServisesAPI"]
            logging.info("SETTINGS_CONFIG: Initialization successful.")
        except:
            logging.error("SETTINGS_CONFIG: Initialization error.")
            print(Fore.RED+"SETTINGS_CONFIG: Initialization error.")
            sys.exit()
        
        try:
            self.addons_support_status = self.addons_cfg["app_addons"]["addons_support_status"]
            self.addons_user_auth_system_status = self.addons_cfg["app_addons"]["addons_user_auth_system_status"]
            self.addons_need_user_plan_to_run = self.addons_cfg["app_addons"]["addons_need_user_plan_to_run"]
            self.addons_SXSC_Security = self.addons_cfg["app_addons"]["SXSC-Security"]
            self.addons_SXSC_Analytics = self.addons_cfg["app_addons"]["SXSC-Analytics"]
            self.addons_SXSC_Optimizer = self.addons_cfg["app_addons"]["SXSC-Optimizer"]
            self.addons_SXSC_Monitoring = self.addons_cfg["app_addons"]["SXSC-Monitoring"]
            self.addons_SXSC_Integration = self.addons_cfg["app_addons"]["SXSC-Integration"]
            self.addons_SXSC_Storage = self.addons_cfg["app_addons"]["SXSC-Storage"]
            logging.info("ADDONS_CONFIG: Initialization successful.")
        except:
            logging.error("ADDONS_CONFIG: Initialization error.")
            print(Fore.RED+"ADDONS_CONFIG: Initialization error.")
            sys.exit()
        
        try:
            self.auth_control_api_path = self.api_cfg["app_api_settings"]["Auth_Control_API_path"]
            self.version_control_api_path = self.api_cfg["app_api_settings"]["Version_Control_API_path"]
            self.cloud_control_api_path = self.api_cfg["app_api_settings"]["Cloud_Control_API_path"]
            self.analytics_control_api_path = self.api_cfg["app_api_settings"]["Analytics_Control_API_path"]
            self.servise_status_api_path = self.api_cfg["app_api_settings"]["Servise_Status_API_path"]
            self.api_settings_security_auth = self.api_cfg["app_api_settings"]["Settings"]["Security"]["AUTH"]
            self.api_settings_security_ssl = self.api_cfg["app_api_settings"]["Settings"]["Security"]["SSL"]
            self.api_settings_methods_support_get = self.api_cfg["app_api_settings"]["Settings"]["MetodsSupport"]["GET"]
            self.api_settings_methods_support_post = self.api_cfg["app_api_settings"]["Settings"]["MetodsSupport"]["POST"]
            self.api_settings_methods_support_put = self.api_cfg["app_api_settings"]["Settings"]["MetodsSupport"]["PUT"]
            self.api_settings_methods_support_delete = self.api_cfg["app_api_settings"]["Settings"]["MetodsSupport"]["DELETE"]
            self.api_settings_methods_support_others = self.api_cfg["app_api_settings"]["Settings"]["MetodsSupport"]["Others"]
            self.api_statuses_logging = self.api_cfg["app_api_settings"]["Settings"]["API_STATUSES_LOGGINING"]
            logging.info("API_CONFIG: Initialization successful.")
        except:
            logging.error("API_CONFIG: Initialization error.")
            print(Fore.RED+"API_CONFIG: Initialization error.")
            sys.exit()
            
        try:
            self.localhost_default_port = self.localhost_cfg["local_host"]["default_port"]
            self.local_hosting_support = self.localhost_cfg["local_host"]["local_hosting_support"]
            self.localhost_default_path = self.localhost_cfg["local_host"]["default_path"]
            logging.info("LOCALHOST_CONFIG: Initialization successful.")
        except:
            logging.error("LOCALHOST_CONFIG: Initialization error.")
            print(Fore.RED+"LOCALHOST_CONFIG: Initialization error.")
            sys.exit()
        
        try:
            self.session_id=random.randint(1,9999999)
            logging.info(f"SESSION_ID: Initialization successful. ID: {self.session_id}")
        except:
            logging.error("SESSION_ID: Initialization error.")
            print(Fore.RED+"SESSION_ID: Initialization error.")
            sys.exit()
        
        try:
            self.input_color = color_map.get(self.pers_cfg["CLI"]["input_color"], Fore.BLUE)
            self.logo_color = color_map.get(self.pers_cfg["CLI"]["logo_color"], Fore.GREEN)
            self.errors_color = color_map.get(self.pers_cfg["CLI"]["errors_color"], Fore.RED)
            self.startmenu_color = color_map.get(self.pers_cfg["CLI"]["start_menu_color"], Fore.WHITE)
            self.show_version=self.pers_cfg["CLI"]["show_version"]
            logging.info("PERS_CONFIG: Initialization successful.")
        except:
            logging.error("PERS_CONFIG: Initialization error.")
            print(Fore.RED+"PERS_CONFIG: Initialization error.")
            sys.exit()    
        
        if SXServiseCLI.check_internet(self)==True:
            logging.info("There is an Internet connection")
        elif SXServiseCLI.check_internet(self)==False:
            logging.warning("No internet connection.")
        
        logging.info("Initialization successful.")
        
        try:
            if ctypes.windll.shell32.IsApplicationUserModelIDSupported():
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.app_com)
            pass
        except:
            pass
        finally:
            if other=="run":
                SXServiseCLI.run(self)
            else:
                SXServiseCLI.System.run_command(self, command=other)
        
    def check_internet(self):
        try:
            socket.create_connection(("www.google.com", 80), timeout=5)
            return True
        except OSError:
            return False
        
    def create_folder_if_not_exists(self,folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        else:
            pass
    
    def check_and_create_json(self,file_name, data):
        if not os.path.isfile(file_name):
            with open(file_name, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        else:
            pass
        
    def save_user_data(self, full_name, nickname, email, password, need_password):
        data = {
            "fullname": full_name,
            "nickname": nickname,
            "password": password,
            "mail": email,
            "MODE": 0,
            "need_password_": need_password
        }
        with open("System/configs/user.cfg.json", "w") as data_q:
            json.dump(data, data_q)
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.logo_color+self.logo)
        print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
        logging.info("CLI: Successfully launched.")
        if self.user_cfg["fullname"]=="x" or self.user_cfg["nickname"]=="x" or self.user_cfg["mail"]=="x":
            print(self.startmenu_color+"")
            print(Fore.WHITE+"Registration in the application: ")
            
            full_name = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Enter your full name:", default="John Doe")
            nickname = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Enter your nickname:", default="John")
            email = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Enter your email:", default="example@example.com")
            password = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Enter your password:", password=True)
            np = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Would you like to ask for your password at startup? (Y/N):", default="Y")
            
            need_password = np.lower() == "y"
            self.save_user_data(full_name, nickname, email, password, need_password)
            print(" ")
            print(Fore.GREEN+"Registration is successful!")
            logging.info("CLI: Registration is successful.")
            print(self.startmenu_color+" ")
            SXServiseCLI.System.run_input(self)
                
        elif self.user_cfg["need_password_"]:
            print(" ")
            if str(input(self.input_color+" - Enter password: ")) == self.user_cfg["password"]:
                print(" ")
                print(self.startmenu_color+f" Welcome, {self.user_cfg['nickname']}!")
                print(self.startmenu_color+" Do you need help? -> help")
                print(self.startmenu_color+" All you need in one place")
                print(" ")
                SXServiseCLI.System.run_input(self)
            else:
                print(self.errors_color+" -> Incorrect password try again later!")
                logging.warning("CLI: Incorrect password")
                time.sleep(4)
                sys.exit()
                
        else:
            print(self.startmenu_color+f" Welcome, {self.user_cfg['nickname']}!")
            print(self.startmenu_color+" Do you need help? -> help")
            print(self.startmenu_color+" All you need in one place")
            print(" ")
            SXServiseCLI.System.run_input(self)
    
    class System:
        
        def pers(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color + self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(" ")

            print(f"""
            Personalization:
            - Logo color   -> {Fore.WHITE + self.pers_cfg["CLI"]["logo_color"]}
            - Input color   -> {Fore.WHITE + self.pers_cfg["CLI"]["input_color"]}
            - Errors color  -> {Fore.WHITE + self.pers_cfg["CLI"]["errors_color"]}
            - Start menu color -> {Fore.WHITE + self.pers_cfg["CLI"]["start_menu_color"]}
            - Show version -> {str(Fore.WHITE + str(self.pers_cfg["CLI"]["show_version"]))}
            
            Actions:
            - Change colors -> custom -r -colors
            - Change other  -> custom -r -other
            - Return to menu -> return
        """)
            logging.info("Component PERS: Successfully launched.")
            action = input(Fore.WHITE + " - Choose an action (colors/other/return): ").strip().lower()

            if action == "colors":
                logo_color = input(Fore.WHITE + " - Enter new logo color: ").strip().upper()
                input_color = input(Fore.WHITE + " - Enter new input color: ").strip().upper()
                errors_color = input(Fore.WHITE + " - Enter new errors color: ").strip().upper()
                start_menu_color = input(Fore.WHITE + " - Enter new start menu color: ").strip().upper()

                self.pers_cfg["CLI"]["logo_color"] = logo_color
                self.pers_cfg["CLI"]["input_color"] = input_color
                self.pers_cfg["CLI"]["errors_color"] = errors_color
                self.pers_cfg["CLI"]["start_menu_color"] = start_menu_color
                
                with open("System/configs/personalization.cfg.json", "w") as pers_file:
                    json.dump(self.pers_cfg, pers_file, indent=4)
                
                print(Fore.GREEN + "Colors updated successfully!")
                SXServiseCLI.System.run_input(self)

            elif action == "other":
                show_version = input(Fore.WHITE + " - Show version at startup? (true/false): ").strip().lower()
                self.pers_cfg["CLI"]["show_version"] = show_version == "true"
                
                with open("System/configs/personalization.cfg.json", "w") as pers_file:
                    json.dump(self.pers_cfg, pers_file, indent=4)
                
                print(Fore.GREEN + "Settings updated successfully!")
                logging.info("Component Pers: Settings updated successfully!")
                SXServiseCLI.System.run_input(self)

            elif action == "return":
                SXServiseCLI.System.run_input(self)

            else:
                print(Fore.RED + " - 404. Command error.")
                logging.error("Component Pers: 404. Command error.")
                SXServiseCLI.System.run_input(self)
        
        def config(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color + self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(" ")
            print(Fore.WHITE + " Welcome to SXSCLI:CONFIG!")
            logging.info("Component CONFIG: Successfully launched.")
            tree = Tree("[blue]Your Current Configuration:", style="bold green")
            tree.box = box.SQUARE
            tree.add("[cyan]Addons Configuration: [white]{}".format(path_addons_cfg))
            tree.add("[cyan]API Configuration: [white]{}".format(path_api_cfg))
            tree.add("[cyan]Localhost Configuration: [white]{}".format(path_localhost_cfg))
            tree.add("[cyan]Personalization Configuration: [white]{}".format(path_pers_cfg))
            tree.add("[cyan]System Configuration: [white]{}".format(path_system_cfg))
            
            self.console.print(tree)
            print(" ")
            SXServiseCLI.System.run_input(self)
                
        class CyberSecurity:
            class cryption:
                pass
                
            class pscan:
                def scan_port(self, host, port):
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.settimeout(1)
                            result = s.connect_ex((host, port))
                            if result == 0:
                                logging.info(f"Component PORTSCAN: Port {port} is OPEN")
                                return f" - Port {port} is OPEN"
                            else:
                                logging.info(f"Component PORTSCAN: Port {port} is CLOSED")
                                return f" - Port {port} is CLOSED"
                            
                    except Exception as e:
                        logging.error(f"Component PORTSCAN: Error scanning port {port}: {e}")
                        return f" - Error scanning port {port}: {e}"

                def scan_all_ports(self, host, log_path_res):
                    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                        with open(log_path_res, "w", encoding='utf-8') as result_file:
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - SXSCLI: PORTSCAN - Domain: {host}\n")
                            result_file.flush()
                            ports = range(1, 65536)
                            future_to_port = {executor.submit(SXServiseCLI.System.CyberSecurity.pscan.scan_port, self,host, port): port for port in ports}
                            for future in concurrent.futures.as_completed(future_to_port):
                                print(Fore.WHITE+"SXSCLI -> "+future.result())
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - {str(host)} - {future.result()}\n")
                                result_file.flush()
                    result_file.write(f"Thanks for using. \n")
                    result_file.flush()
                    result_file.write(f"Powered by SXServiseCLI. \n")
                    result_file.flush()
                    print(Fore.WHITE+f"Results saved: {log_path_res}")
                    result_file.close()

                def portscan_sxscli(self, target_host):
                    result_path_whois = f"Staff/results/{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}_portcan_result.log"
                    os.makedirs(os.path.dirname(result_path_whois), exist_ok=True)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Fore.WHITE + " - - - - - - - - SXSCLI: PORTSCAN - - - - - - - - ")
                    print(" ")
                    logging.info(f"Component PORTSCAN: Starting a port scan. Domain: {target_host}")
                    
                    try:
                        print(Fore.WHITE + f"Scanning ports on {target_host}...")
                        SXServiseCLI.System.CyberSecurity.pscan.scan_all_ports(self,target_host, result_path_whois)
                    except Exception as e:
                        print(Fore.RED + f"Error scanning ports: {e}")
                        logging.error(f"Component PortScan: Error scanning ports. ERROR: {e}")
                    finally:
                        print(" ")
                        print(Fore.WHITE + " - - - - - - - - - - - - - - - - - - - - - - - - - ")
                        print(Fore.WHITE + " ")
                        SXServiseCLI.System.run_input(self)

                def main(self):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:PORTSCAN!")
                    logging.info("Component PORTSCAN: Successfully launched.")
                    target_host = input(Fore.WHITE + " - Enter host to scan (IP or domain)(or exit): ")
                    if target_host.lower() == "exit":
                        print(Fore.WHITE + " ")
                        SXServiseCLI.System.run_input(self)
                    else:
                        print(Fore.WHITE + " ")
                        SXServiseCLI.System.CyberSecurity.pscan.portscan_sxscli(self,target_host)

            
            class whois:
                def whois_sxscli(self, domain):
                    result_path_whois = f"Staff/results/{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}_whois_result.log"
                    os.makedirs(os.path.dirname(result_path_whois), exist_ok=True)
                    with open(result_path_whois, "w") as result_file:
                        result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - SXSCLI_WHOIS: Domain: {domain}\n")
                        result_file.flush()

                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(Fore.WHITE + " - - - - - - - - SXSCLI: WHOIS - - - - - - - - ")
                        logging.info(f"Component WHOIS: Getting information about a domain: {domain}")
                        try:
                            domain_info = whois.whois(domain)
                            print(Fore.WHITE + "Domain WHOIS info:")
                            for key, value in domain_info.items():
                                print(Fore.WHITE + f" - {key}: {value}")
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Domain_Info: - {key}: {value}\n")
                                result_file.flush()
                        except Exception as e:
                            logging.error(f"Component WHOIS: WHOIS error: {e}")
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component WHOIS: WHOIS error: {e}\n")
                            result_file.flush()
                            print(self.errors_color + f"WHOIS error: {e}")

                        # DNS Records
                        try:
                            print(Fore.WHITE + "\nDNS Records:")
                            a_records = dns.resolver.resolve(domain, 'A')
                            for a in a_records:
                                print(Fore.WHITE + f" - A Record: {a}")
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - A Record: {a}\n")
                                result_file.flush()

                            mx_records = dns.resolver.resolve(domain, 'MX')
                            for mx in mx_records:
                                print(Fore.WHITE + f" - MX Record: {mx.exchange} Priority: {mx.preference}")
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - MX Record: {mx.exchange} Priority: {mx.preference}\n")
                                result_file.flush()

                            txt_records = dns.resolver.resolve(domain, 'TXT')
                            for txt in txt_records:
                                print(Fore.WHITE + f" - TXT Record: {txt.to_text()}")
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - TXT Record: {txt.to_text()}\n")
                                result_file.flush()

                            cname_record = dns.resolver.resolve(domain, 'CNAME')
                            for cname in cname_record:
                                print(Fore.WHITE + f" - CNAME Record: {cname}")
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - CNAME Record: {cname}\n")
                                result_file.flush()
                        except Exception as e:
                            logging.error(f"Component WHOIS: DNS Record error: {e}")
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component WHOIS: DNS Record error: {e}\n")
                            result_file.flush()
                            print(self.errors_color + f"DNS Record error: {e}")

                        try:
                            print(Fore.WHITE + "\nSSL Certificate:")
                            context = ssl.create_default_context()
                            with socket.create_connection((domain, 443)) as sock:
                                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                                    cert = ssock.getpeercert()
                                    print(Fore.WHITE + f" - Issuer: {cert['issuer']}")
                                    print(Fore.WHITE + f" - Valid from: {cert['notBefore']}")
                                    print(Fore.WHITE + f" - Valid until: {cert['notAfter']}")
                                    print(Fore.WHITE + f" - Serial Number: {cert['serialNumber']}")
                                    print(Fore.WHITE + f" - Signature Algorithm: {cert['signatureAlgorithm']}")
                            
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Issuer: {cert['issuer']} - Valid from: {cert['notBefore']} - Valid until: {cert['notAfter']} - Serial Number: {cert['serialNumber']} - Signature Algorithm: {cert['signatureAlgorithm']}\n")
                            result_file.flush()
                        except Exception as e:
                            logging.error(f"Component WHOIS: SSL error: {e}")
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component WHOIS: SSL error: {e}\n")
                            result_file.flush()
                            print(self.errors_color + f"SSL error: {e}")

                        try:
                            print(Fore.WHITE + "\nEmail Security Records:")
                            txt_records = dns.resolver.resolve(domain, 'TXT')
                            for txt in txt_records:
                                if 'v=spf' in txt.to_text():
                                    print(Fore.WHITE + f" - SPF Record: {txt.to_text()}")
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - SPF Record: {txt.to_text()}\n")
                                    result_file.flush()
                                if 'v=DMARC' in txt.to_text():
                                    print(Fore.WHITE + f" - DMARC Record: {txt.to_text()}")
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - DMARC Record: {txt.to_text()}\n")
                                    result_file.flush()

                            dkim_records = dns.resolver.resolve(f"{domain}._domainkey.{domain}", 'TXT')
                            for dkim in dkim_records:
                                print(Fore.WHITE + f" - DKIM Record: {dkim.to_text()}")
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - DKIM Record: {dkim.to_text()}\n")
                                result_file.flush()
                        except Exception as e:
                            logging.error(f"Component WHOIS: Email Security Record error: {e}")
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component WHOIS: Email Security Record error: {e}\n")
                            result_file.flush()
                            print(self.errors_color + f"Email Security Record error: {e}")

                        result_file.write("Thanks for using.\n")
                        result_file.write("Powered by SXServiseCLI.\n")
                        result_file.flush()
                        result_file.close()
                        print(f"The results are saved: {result_path_whois}")
                        print(Fore.WHITE + " - - - - - - - - - - - - - - - - - - - - - - - ")
                        SXServiseCLI.System.run_input(self)
                        
                def main(self):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color+self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE+" Welcome to SXSCLI:WHOIS!")
                    logging.info("Component WHOIS: Successfully launched.")
                    domain = input(self.input_color+" - Enter domain name (Or exit): ")
                    if domain.lower()=="exit":
                        print(Fore.WHITE+" ")
                        SXServiseCLI.System.run_input(self)
                    else:
                        print(Fore.WHITE+" ")
                        SXServiseCLI.System.CyberSecurity.whois.whois_sxscli(self, domain)

            
        def upgrade(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color+self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(Fore.WHITE+" Welcome to SXSCLI:UPGRADE!")
            logging.info("Component UPGRADE: Successfully launched.")
            print(Fore.WHITE+f"""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                Welcome to the SXSCLI Upgrade Center!     ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ┌─────────────────────────────────────────────────────────┐
    │ Your Current Version:                                   │
    │ SXSCLI - Version: {self.app_version}                             │
    └─────────────────────────────────────────────────────────┘

    🔹 Upgrades Available Just for You:
       ────────────────────────────────────────────
       1. SXSCLI+  ->   $2.99 
          → Unlock advanced tools, faster speeds, and custom themes!
       2. SXSCLI-Pro  ->   $7.99
          → Gain access to exclusive modules, priority support, 
             and the full suite of SXSCLI features!
             
    ┌─────────────────────────────────────────────────────────┐
    │      Ready to Upgrade?                                  │
    │   Visit the links below to learn more and upgrade:      │
    └─────────────────────────────────────────────────────────┘
    🌐 Official Website: https://sxcomp.42web.io/p/SXServiseCLI
    🛒 Version Store: https://ko-fi.com/stasx/shop
""")
            SXServiseCLI.System.run_input(self)
        
        def help(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color+self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(Fore.WHITE+" Welcome to SXSCLI:HELP!")
            logging.info("Component HELP: Successfully launched.")
            print(Fore.WHITE+
"""
- - - - - - - - - - - - - - Global list of commands - - - - - - - - - - - - - -      < - - - Global* commands
   help - Global list of commands
   info - Assembly information
   init - Initialize the application
   support - Official technical support
   pers - Personalization settings
   config - Configuration settings
   upgrade - Buy a better version
 - - - - - - - - - - - - - - - - CYBER SECURITY - - - - - - - - - - - - - - - -      < - - - Dangerous* commands
   whois - Domain check
   pscan - Port scan
 - - - - - - - - - - - - - - - - - - TOOLS - - - - - - - - - - - - - - - - - - -     < - - - Internal tools 
   ftp - File Transfer Protocol client (FTP)
   ssh - Secure Shell protocol client (SSH)
   ping - Ping server (PING)
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  - Dangerous* - You take full responsibility for your actions
  - Global* - System commands with CLI
 Copyright (c) 2023-2024 Kozosvyst Stas (StasX) 
""")
            SXServiseCLI.System.run_input(self)
        
        def support(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color+self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(" ")
            print(Fore.WHITE+" Welcome to SXSCLI:SUPPORT!")
            logging.info("Component SUPPORT: Successfully launched.")
            print(Fore.WHITE+
"""
Are you having problems?
 - Problems with using: https://github.com/StasX-Official/SXServiseCLI/wiki
 - Ideas for improvement and questions: https://github.com/StasX-Official/SXServiseCLI/discussions
 - Report a vulnerability: https://github.com/StasX-Official/SXServiseCLI/pulls
 - Report a violation: sxservise@outlook.com
 - Other questions: sxservise@outlook.com

We apologize for the inconvenience.
Thank you for using.
""")
            SXServiseCLI.System.run_input(self)
        
        def info(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color+self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(" ")
            print(Fore.WHITE+" Welcome to SXSCLI:INFO!")
            logging.info("Component INFO: Successfully launched.")
            try:
                user_ip=str(socket.gethostbyname(socket.gethostname()))
            except:
                user_ip="ERROR"
            finally:
                print(Fore.WHITE+
f"""- - - - - - - - - - - - - - - -  User Info - - - - - - - - - - - - - - - - - - -
    Nickname - {self.user_cfg["nickname"]}
    FullName - {self.user_cfg["fullname"]}
    Mail - {self.user_cfg["mail"]}
    IP - {user_ip} - Mode - {self.user_cfg["MODE"]}  
- - - - - - - - - - - - - - - - - CLI Info - - - - - - - - - - - - - - - - - - -
    CLI Name - {self.app_name} 
    CLI Version - {self.app_version}
    CLI ID - {self.app_id}
    CLI COM - {self.app_com}
    CLI API - {str(self.settings_api)}
    CLI AuthAPI - {str(self.settings_AuthAPI)}
    CLI ServisesAPI - {str(self.settings_ServisesAPI)}
    - - - - - - - - - - - - - - - - - LINKS - - - - - - - - - - - - - - - - - -
     - GitHub: https://github.com/StasX-Official/SXServiseCLI
     - Official site: https://sxcomp.42web.io/p/SXServiseCLI
     - Official wiki: https://github.com/StasX-Official/SXServiseCLI/wiki
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
""")
            SXServiseCLI.System.run_input(self)
            
        class ping:
            def ping(self,host):
                param = "-n" if platform.system().lower() == "windows" else "-c"
                command = ["ping", param, "4", host]
                try:
                    output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
                    print(f"Ping to {host} was successful.")
                    print(output)
                    print(" ")
                    logging.info(f"Component PING: Ping to {host} was successful. Result: {output}")
                    SXServiseCLI.System.run_input(self)
                    
                except subprocess.CalledProcessError as e:
                    print(f"Ping to {host} failed.")
                    print(e.output)
                    print(" ")
                    logging.error(f"Component PING: Ping to {host} failed.")
                    SXServiseCLI.System.run_input(self)
                    
            def main(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color+self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(" ")
                print(Fore.WHITE+" Welcome to SXSCLI:PING!")
                logging.info("Component PING: Successfully launched.")
                host = str(input(self.input_color+" - Enter Host to ping (or exit): "))
                if host.lower()=="exit":
                    print(Fore.WHITE+" ")
                    SXServiseCLI.System.run_input(self)
                else:
                    print(Fore.WHITE+" ")
                    SXServiseCLI.System.ping.ping(self, host)
        
        class ftp:
            def run(self):
                result_path_ftp = f"Staff/results/{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}_ftp_result.log"
                os.makedirs(os.path.dirname(result_path_ftp), exist_ok=True)
                with open(result_path_ftp, "w", encoding='utf-8') as result_file:
                    try:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(self.logo_color+self.logo)
                        print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                        print(" ")
                        print(Fore.WHITE+" Welcome to SXSCLI:FTP!")
                        logging.info("Component FTP: Successfully launched.")
                        ftp_host = str(input(self.input_color+" - Enter FTP Host: "))
                        ftp_username = str(input(self.input_color+" - Enter FTP username: "))
                        ftp_password = str(input(self.input_color+" - Enter FTP password: "))
                        def connect_ftp(host, username, password):
                            ftp = FTP(host)
                            ftp.login(username, password)
                            print(f"Successful connection to the FTP server")
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Successful connection to the FTP server. HOST: {ftp_host}\n")
                            result_file.flush()
                            logging.info(f"FTP: Successful connection to the FTP server. HOST: {ftp_host}")
                            set_passive_mode(ftp)
                            return ftp


                        def set_passive_mode(ftp):
                            ftp.set_pasv(True)


                        def execute_ftp_command(ftp, command):
                            result = ""

                            if command.upper() == "QUIT":
                                ftp.quit()
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Connection to the FTP server has been terminated. HOST: {ftp_host}\n")
                                result_file.flush()
                                print("Connection to the FTP server has been terminated.")
                                input_command = command()
                            elif command.upper() == "LIST":
                                result = ftp.retrlines("LIST")
                                print(f"Result of executing 'LIST' command:\n{result}")
                            else:
                                result = ftp.sendcmd(command)
                                print(f"Result of executing '{command}': {result}")
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Result: {result}\n")
                            result_file.flush()
                            return result


                        ftp_connection = connect_ftp(ftp_host, ftp_username, ftp_password)

                        while True:
                            user_input = input(self.input_color+"Enter the command to execute on FTP (QUIT to exit): ")
                            logging.info(f"FTP: The user launched the command: {user_input}")
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - The user launched the command: {user_input}\n")
                            result_file.flush()
                            execute_ftp_command(ftp_connection, user_input)
                    except:
                        print(self.errors_color+"Error connecting to the FTP server.")
                        logging.error(f"FTP: Error connecting to the FTP server.")
                        result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Error connecting to the FTP server. HOST: {ftp_host}\n")
                        result_file.flush()
                    finally:
                        print(" ")
                        result_file.write(f"Thanks for using!\n")
                        result_file.write(f"Powered by SXServiseCLI!\n")
                        result_file.flush()
                        result_file.close()
                        SXServiseCLI.System.run_input(self)
                    
                 
        class ssh:
            def run(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color+self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(" ")
                print(Fore.WHITE+" Welcome to SXSCLI:SSH!") 
                logging.info("Component SSH: Successfully launched.")
                print(" ")
                if str(input(Fore.WHITE+"Do you want to continue? (connect/exit) >>> ")).lower()=="exit":
                    SXServiseCLI.System.run_input(self)
                    
                ssh_host = str(input(self.input_color+" - Enter SSH Host: "))
                ssh_username = str(input(self.input_color+" - Enter SSH Username: "))
                ssh_password = getpass(self.input_color+" - Enter SSH Password: ")

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                try:
                    ssh.connect(ssh_host, username=ssh_username, password=ssh_password)
                    print(Fore.LIGHTGREEN_EX+f"Successful connection to {ssh_host}\n")
                    logging.info(f"SSH: Successful connection to {ssh_host}")

                    while True:
                        command = input(self.input_color+"Enter the command (or 'help' for available commands, 'exit' to quit): ")
                        logging.info(f"SSH: The user launched the command: {command}")

                        if command.lower() == "exit":
                            break

                        elif command.lower() == "help":
                            print(Fore.LIGHTGREEN_EX + """Available commands:
  help            - Show this help message
  exit            - Exit the SSH session
  ls              - List directory contents
  pwd             - Print the current working directory
  whoami          - Show the current user
  df              - Show disk space usage
  uptime          - Show how long the system has been running
  free            - Show memory usage
  uname           - Show system information
  top             - Display system processes
  date            - Show the current date and time
  df -i           - Show inode usage
  grep            - Search for a pattern in files
  find            - Search for files in a directory hierarchy
  cat             - Concatenate and display file content
  head            - Show the first few lines of a file
  tail            - Show the last few lines of a file
  man             - Show the manual for a command
  chmod           - Change file permissions
  chown           - Change file owner and group
  ps              - Display information about active processes
  kill            - Kill a process by ID
  tar             - Archive files
  df -h           - Show human-readable disk space usage
  lsof            - List open files
  history         - Show command history
  ifconfig        - Display network configuration
  ip              - Show or manipulate routing, devices, policy routing, and tunnels
  netstat         - Print network connections, routing tables, interface statistics
  ssh-keygen      - Generate a new SSH key pair
  curl            - Transfer data from or to a server
  wget            - Retrieve files from the web
  top -o          - Sort top output by a specific field (e.g., %MEM)
  df -T           - Show filesystem type
  du              - Show disk usage of files and directories
  dd              - Convert and copy files
  lsblk           - List information about block devices
  mount           - Mount a filesystem
  umount          - Unmount a filesystem
  systemctl       - Control the systemd system and service manager
  journalctl      - Query and display messages from the journal
  crontab         - Manage cron jobs
  rsync           - Sync files and directories
  chmod +x        - Make a script executable
  stat            - Display file or file system status
  df -hT          - Show human-readable filesystem type
  du -sh          - Show disk usage in human-readable format
  find /path -exec cmd {} \\; - Execute a command on files found
  du -a           - Show disk usage of all files
  sort            - Sort lines of text files
  awk             - Pattern scanning and processing language
  sed             - Stream editor for filtering and transforming text
  head -n         - Show the first n lines of a file
  tail -n         - Show the last n lines of a file
  wget -O         - Download file and save with a specific name
  curl -o         - Download file and save with a specific name
  touch           - Create an empty file or update file timestamps
  echo            - Display a line of text
  diff            - Compare files line by line
  file            - Determine file type
  xargs           - Build and execute command lines from standard input
  gzip            - Compress files
  gunzip          - Decompress files
  bzip2           - Compress files using bzip2
  bunzip2         - Decompress files using bzip2
  mkdir           - Create a new directory
  rm              - Remove a file or directory
  mv              - Move or rename files
  cp              - Copy files or directories
  alias           - Create or view command aliases
  unalias         - Remove a command alias
  hostname        - View or change the hostname
  traceroute      - Trace the route to a host
  ping            - Check the availability of a host
  df -h --total   - Show the total disk space usage
  ssh-copy-id     - Copy SSH key to a server
  nano            - Edit files using the Nano editor
  vim             - Edit files using the Vim editor
  du -m           - Show disk usage in megabytes
  tree            - Show directory structure as a tree
  locate          - Find files on the server
  last            - Show the last users who logged in
  uptime -p       - Show the system uptime in a compact format
  uptime -s       - Show when the system was started
  dmesg           - View kernel system messages
  clear           - Clear the terminal screen
  tac             - Display a file in reverse order (last line to first)
  ln              - Create symbolic or hard links
  shutdown        - Perform a system shutdown
  reboot          - Reboot the system
  Any other command will be executed on the server
""")

                            continue
                        
                        elif command.lower() == "mkdir":
                            dir_name = input(Fore.LIGHTGREEN_EX+"Enter directory name to create: ")
                            command = f"mkdir {dir_name}"
                        
                        elif command.lower() == "rm":
                            path = input(Fore.LIGHTGREEN_EX+"Enter file or directory to remove: ")
                            command = f"rm -r {path}"
                        
                        elif command.lower() == "mv":
                            src = input(Fore.LIGHTGREEN_EX+"Enter source file or directory: ")
                            dest = input(Fore.LIGHTGREEN_EX+"Enter destination: ")
                            command = f"mv {src} {dest}"
                        
                        elif command.lower() == "cp":
                            src = input(Fore.LIGHTGREEN_EX+"Enter source file or directory: ")
                            dest = input(Fore.LIGHTGREEN_EX+"Enter destination: ")
                            command = f"cp -r {src} {dest}"
                        
                        elif command.lower() == "alias":
                            command_name = input(Fore.LIGHTGREEN_EX+"Enter alias command: ")
                            command = f"alias {command_name}"
                            
                        elif command.lower() == "unalias":
                            alias_name = input(Fore.LIGHTGREEN_EX+"Enter alias to remove: ")
                            command = f"unalias {alias_name}"
                        
                        elif command.lower() == "hostname":
                            command = "hostname"
                        
                        elif command.lower() == "traceroute":
                            target = input(Fore.LIGHTGREEN_EX+"Enter target host: ")
                            command = f"traceroute {target}"

                        elif command.lower() == "ping":
                            target = input(Fore.LIGHTGREEN_EX+"Enter target host: ")
                            command = f"ping -c 4 {target}"

                        elif command.lower() == "df -h --total":
                            command = "df -h --total"

                        elif command.lower() == "ssh-copy-id":
                            user_host = input(Fore.LIGHTGREEN_EX+"Enter user@host: ")
                            command = f"ssh-copy-id {user_host}"

                        elif command.lower() == "nano":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to edit: ")
                            command = f"nano {file}"
                            
                        elif command.lower() == "vim":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to edit: ")
                            command = f"vim {file}"

                        elif command.lower() == "du -m":
                            directory = input(Fore.LIGHTGREEN_EX+"Enter directory to check usage: ")
                            command = f"du -m {directory}"

                        elif command.lower() == "tree":
                            command = "tree"

                        elif command.lower() == "locate":
                            filename = input(Fore.LIGHTGREEN_EX+"Enter filename to locate: ")
                            command = f"locate {filename}"

                        elif command.lower() == "last":
                            command = "last"

                        elif command.lower() == "uptime -p":
                            command = "uptime -p"
                        
                        elif command.lower() == "uptime -s":
                            command = "uptime -s"
                        
                        elif command.lower() == "dmesg":
                            command = "dmesg"
                        
                        elif command.lower() == "clear":
                            command = "clear"
                        
                        elif command.lower() == "ln":
                            target = input(Fore.LIGHTGREEN_EX+"Enter target file: ")
                            link_name = input(Fore.LIGHTGREEN_EX+"Enter name for the link: ")
                            command = f"ln -s {target} {link_name}"
                        
                        elif command.lower() == "shutdown":
                            command = "shutdown now"
                        
                        elif command.lower() == "reboot":
                            command = "reboot"

                        elif command.lower() == "ls":
                            command = "ls -la"

                        elif command.lower() == "pwd":
                            command = "pwd"

                        elif command.lower() == "whoami":
                            command = "whoami"

                        elif command.lower() == "df":
                            command = "df -h"

                        elif command.lower() == "uptime":
                            command = "uptime"

                        elif command.lower() == "free":
                            command = "free -h"

                        elif command.lower() == "uname":
                            command = "uname -a"

                        elif command.lower() == "top":
                            command = "top -bn1"

                        elif command.lower() == "date":
                            command = "date"

                        elif command.lower() == "df -i":
                            command = "df -i"

                        elif command.lower() == "grep":
                            pattern = input(Fore.LIGHTGREEN_EX+"Enter pattern to search: ")
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to search in: ")
                            command = f"grep '{pattern}' {file}"

                        elif command.lower() == "find":
                            directory = input(Fore.LIGHTGREEN_EX+"Enter directory to search in: ")
                            search = input(Fore.LIGHTGREEN_EX+"Enter file or pattern to search for: ")
                            command = f"find {directory} -name {search}"

                        elif command.lower() == "cat":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to display: ")
                            command = f"cat {file}"

                        elif command.lower() == "head":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to display: ")
                            lines = input(Fore.LIGHTGREEN_EX+"Enter number of lines to display: ")
                            command = f"head -n {lines} {file}"

                        elif command.lower() == "tail":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to display: ")
                            lines = input(Fore.LIGHTGREEN_EX+"Enter number of lines to display: ")
                            command = f"tail -n {lines} {file}"

                        elif command.lower() == "man":
                            cmd = input(Fore.LIGHTGREEN_EX+"Enter command to display manual: ")
                            command = f"man {cmd}"

                        elif command.lower() == "chmod":
                            permissions = input(Fore.LIGHTGREEN_EX+"Enter permissions (e.g., 755): ")
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to change permissions: ")
                            command = f"chmod {permissions} {file}"

                        elif command.lower() == "chown":
                            owner = input(Fore.LIGHTGREEN_EX+"Enter new owner: ")
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to change owner: ")
                            command = f"chown {owner} {file}"

                        elif command.lower() == "ps":
                            command = "ps aux"

                        elif command.lower() == "kill":
                            pid = input(Fore.LIGHTGREEN_EX+"Enter process ID to kill: ")
                            command = f"kill {pid}"

                        elif command.lower() == "tar":
                            options = input(Fore.LIGHTGREEN_EX+"Enter tar options (e.g., -czvf): ")
                            archive = input(Fore.LIGHTGREEN_EX+"Enter archive name: ")
                            files = input(Fore.LIGHTGREEN_EX+"Enter files to archive: ")
                            command = f"tar {options} {archive} {files}"

                        elif command.lower() == "df -h":
                            command = "df -h"

                        elif command.lower() == "lsof":
                            command = "lsof"

                        elif command.lower() == "history":
                            command = "history"

                        elif command.lower() == "ifconfig":
                            command = "ifconfig"

                        elif command.lower() == "ip":
                            command = "ip a"

                        elif command.lower() == "netstat":
                            command = "netstat -tuln"

                        elif command.lower() == "ssh-keygen":
                            command = "ssh-keygen"

                        elif command.lower() == "curl":
                            url = input(Fore.LIGHTGREEN_EX+"Enter URL: ")
                            command = f"curl {url}"

                        elif command.lower() == "wget":
                            url = input(Fore.LIGHTGREEN_EX+"Enter URL: ")
                            command = f"wget {url}"

                        elif command.lower() == "top -o":
                            field = input(Fore.LIGHTGREEN_EX+"Enter field to sort by (e.g., %MEM): ")
                            command = f"top -o {field}"

                        elif command.lower() == "df -T":
                            command = "df -T"

                        elif command.lower() == "du":
                            directory = input(Fore.LIGHTGREEN_EX+"Enter directory to check usage: ")
                            command = f"du -sh {directory}"

                        elif command.lower() == "touch":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to create or update: ")
                            command = f"touch {file}"

                        elif command.lower() == "echo":
                            text = input(Fore.LIGHTGREEN_EX+"Enter text to display: ")
                            command = f"echo {text}"

                        elif command.lower() == "diff":
                            file1 = input(Fore.LIGHTGREEN_EX+"Enter first file to compare: ")
                            file2 = input(Fore.LIGHTGREEN_EX+"Enter second file to compare: ")
                            command = f"diff {file1} {file2}"

                        elif command.lower() == "file":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to determine type: ")
                            command = f"file {file}"

                        elif command.lower() == "xargs":
                            cmd = input(Fore.LIGHTGREEN_EX+"Enter command to execute: ")
                            command = f"xargs {cmd}"

                        elif command.lower() == "gzip":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to compress: ")
                            command = f"gzip {file}"

                        elif command.lower() == "gunzip":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to decompress: ")
                            command = f"gunzip {file}"

                        elif command.lower() == "bzip2":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to compress: ")
                            command = f"bzip2 {file}"

                        elif command.lower() == "bunzip2":
                            file = input(Fore.LIGHTGREEN_EX+"Enter file to decompress: ")
                            command = f"bunzip2 {file}"

                        stdin, stdout, stderr = ssh.exec_command(command)
                        output = stdout.read().decode("utf-8")
                        error = stderr.read().decode("utf-8")

                        if output:
                            print(Fore.LIGHTGREEN_EX + output)
                            logging.info(f"SSH: The component provided the response: {output}")
                        if error:
                            print(Fore.RED + error)
                            logging.error(f"SSH: The component has given an error: {error}")

                except Exception as e:
                    print(self.errors_color+f"Error connecting to the SSH server: {e}")
                    print(" ")
                    logging.error(f"Error connecting to the SSH server: {e}")
                    SXServiseCLI.System.run_input(self)
                
                finally:
                    print(" ")
                    SXServiseCLI.System.run_input(self)
        
        def run_command(self, command):
            logging.info("Launching the component: Entering the command")
            try:
                if command.lower() == "exit":
                    time.sleep(1)
                    sys.exit()
                elif command.lower() == "ssh":
                    SXServiseCLI.System.ssh.run(self)
                elif command.lower() == "ftp":
                    SXServiseCLI.System.ftp.run(self)
                elif command.lower() == "help":
                    SXServiseCLI.System.help(self)
                elif command.lower() == "info":
                    SXServiseCLI.System.info(self)
                elif command.lower() == "support":
                    SXServiseCLI.System.support(self)
                elif command.lower() == "init":
                    SXServiseCLI("run")
                elif command.lower() == "config":
                    SXServiseCLI.System.config(self)
                elif command.lower() == "pers":
                    SXServiseCLI.System.pers(self)
                elif command.lower() == "whois":
                    SXServiseCLI.System.CyberSecurity.whois.main(self)
                elif command.lower() == "pscan":
                    SXServiseCLI.System.CyberSecurity.pscan.main(self)
                elif command.lower() == "upgrade":
                    SXServiseCLI.System.upgrade(self)
                elif command.lower() == "ping":
                    SXServiseCLI.System.ping.main(self)
                else:
                    print(self.errors_color+" - 404. Command not found. ")
                    logging.error(f"404. Command: {command} not found.")
                    SXServiseCLI.System.run_input(self)
            except Exception as e:
                print(self.errors_color+f" - Error: {e}")
                logging.error(f"Error: {e}")
                SXServiseCLI.System.run_input(self)
        
        def run_input(self):
            try:
                cmd=input(self.input_color+" $ >>> ")
                SXServiseCLI.System.run_command(self, command=cmd) 
            except:
                print(self.errors_color+" - Input command error. ")
                logging.critical("Input command error")
                time.sleep(5)
                sys.exit()