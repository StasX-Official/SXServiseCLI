import json, sys, os, time, random, socket, re, logging, platform, subprocess, uuid
import psutil, shutil, requests, GPUtil, ctypes, faker
import mysql.connector, sqlite3
import dns.resolver, ssl, whois
from datetime import datetime
import speedtest
from ftplib import FTP
import concurrent.futures
from colorama import Fore, init
import xml.etree.ElementTree as ET
from rich.console import Console
from rich.prompt import Prompt
from rich.tree import Tree
from rich.panel import Panel
from rich.table import Table
from rich import box
import string
import google.generativeai as genai
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import qrcode, qrcode.image.svg
from PIL import Image
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

from System.media.logo import sxscli_logo_
from System.color_map import color_map
from System.commands_map import command_list
from System.cfg_path_map import path_addons_cfg, path_api_cfg, path_system_cfg, path_localhost_cfg, path_user_cfg, path_pers_cfg
from System import sxscli_core
from System.genai_core import SXSCLI_GENAI
from System.faker_core import SXSCLI_Faker
from System.project_core import SXSCLI_Project
from System.sxscli_web_core import AI_WITH_WEB_INTERFACE
from System.search_engine import Search
from System.sxscli_core import System

try:
    import paramiko
except:
    ssh_status=False
    
init(autoreset=True)

SXSCLICS=System()
firebase_client = SXSCLICS.sxscli.Firebase.Client.Auth(SXSCLICS)

class SXServiseCLI:
    def __init__(self, other):
        self.start_start_time_deb = time.time()
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
            
        with open("System/default/genai_d_s.json", "r") as cache_def_json_ga:
            self.genai_def_settings = json.load(cache_def_json_ga)

        self.cli_commands_list=command_list
        self.send_statistics_status=self.pers_cfg["APP"]["send_statistics"]
        
        if self.pers_cfg["CLI"]["command_autocompletion"]==False:
            self.sxscli_completer_status = False
        else:
            self.sxscli_completer_status = True
            self.completer = WordCompleter(self.cli_commands_list, ignore_case=True)
        
        self.logo=sxscli_logo_
        cont_debug_json={
    "debug_status": False,
    "debug_settings": {
        "level_": "INFO",
        "show_debug_message": False,
        "format": "%(asctime)s - %(name)s - %(levelname)s - SXSCLI: %(message)s"
    }
}
        cont_search_json = {
    "mode": "analyze",
    "engine": "duckduckgo",
    "google_search_engine_api_key": "none",
    "google_search_engine_cse_id": "none",
    "bing_search_api_key": "none"
}
        self.staff_path=self.system_cfg["STAFF"]["path"]
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path)
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/logs")
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/results")
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/projects")
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/dlc")
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/ai")
        SXServiseCLI.create_folder_if_not_exists(self, self.staff_path+"/databases")
        SXServiseCLI.check_and_create_json(self, self.staff_path+"/debug.json", cont_debug_json)
        SXServiseCLI.check_and_create_json(self, self.staff_path+"/search_settings.json", cont_search_json)
        with open(f"{self.staff_path}/debug.json","r") as cache_fdfdfqqqqq:
            self.debug_cfg = json.load(cache_fdfdfqqqqq)
        
        with open(f"{self.staff_path}/search_settings.json", "r") as cache_fdfdfqqqqq:
            search_settings = json.load(cache_fdfdfqqqqq)
                
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
        
        self.search_engine=Search(search_settings)
        
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
            self.warnings = self.system_cfg["warnings"]
            logging.info("SETTINGS_CONFIG: Initialization successful.")
        except Exception as e:
            logging.error(f"SETTINGS_CONFIG: Initialization error. {e}")
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
        except Exception as e:
            logging.error(f"ADDONS_CONFIG: Initialization error. {e}")
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
        except Exception as e:
            logging.error(f"API_CONFIG: Initialization error. {e}")
            print(Fore.RED+"API_CONFIG: Initialization error.")
            sys.exit()
            
        try:
            self.localhost_default_port = self.localhost_cfg["local_host"]["default_port"]
            self.local_hosting_support = self.localhost_cfg["local_host"]["local_hosting_support"]
            self.localhost_default_path = self.localhost_cfg["local_host"]["default_path"]
            logging.info("LOCALHOST_CONFIG: Initialization successful.")
        except Exception as e:
            logging.error(f"LOCALHOST_CONFIG: Initialization error. {e}")
            print(Fore.RED+"LOCALHOST_CONFIG: Initialization error.")
            sys.exit()
        
        try:
            self.session_id=random.randint(1,9999999)
            logging.info(f"SESSION_ID: Initialization successful. ID: {self.session_id}")
        except Exception as e:
            logging.error(f"SESSION_ID: Initialization error. {e}")
            print(Fore.RED+"SESSION_ID: Initialization error.")
            sys.exit()
            self.connection = None
            self.cursor = None
        try:
            self.input_color = color_map.get(self.pers_cfg["CLI"]["input_color"], Fore.BLUE)
            self.logo_color = color_map.get(self.pers_cfg["CLI"]["logo_color"], Fore.GREEN)
            self.errors_color = color_map.get(self.pers_cfg["CLI"]["errors_color"], Fore.RED)
            self.startmenu_color = color_map.get(self.pers_cfg["CLI"]["start_menu_color"], Fore.WHITE)
            self.show_version=self.pers_cfg["CLI"]["show_version"]
            self.checking_for_updates=self.pers_cfg["CLI"]["checking_for_updates"]
    
            if SXServiseCLI.check_internet(self)==True:
                logging.info("There is an Internet connection")
            elif SXServiseCLI.check_internet(self)==False:
                logging.warning("No internet connection.")
            
            if self.checking_for_updates and SXServiseCLI.check_internet(self) == True:
                filename = f"{self.staff_path}/version.json"
                v_data = {
                    "app_version": self.app_version,
                    "last_version": None,
                    "update_checking_time": None
                }
                
                if not os.path.isfile(filename):
                    with open(filename, 'w') as file:
                        json.dump(v_data, file)
                
                try: 
                    with open(filename, 'r') as file:
                        v_data = json.load(file)
                    
                    if (v_data["last_version"] is None or 
                        v_data["update_checking_time"] is None or 
                        (time.time() - v_data["update_checking_time"]) > 86400):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(Fore.WHITE + "SXSCLI: Checking for updates...")

                        options = Options()
                        options.add_argument('--headless')
                        options.add_argument('--disable-dev-shm-usage')
                        options.add_argument('--no-sandbox')
                        options.add_argument('--log-level=3')
                        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                        driver.get("https://www.sxcomp.42web.io/p/SXServiseCLI/apip/getlastversionfree.html")
                        try:
                            last_version = WebDriverWait(driver, 1).until(
                                EC.presence_of_element_located((By.ID, "version"))
                            ).text

                        except Exception as e:
                            logging.error(f"Could not find the version on the page. Error: {e}")

                        finally:
                            driver.quit()
                            v_data["last_version"] = last_version
                            v_data["update_checking_time"] = time.time()
                            self.update_checking_status = last_version
                            
                            with open(filename, 'w') as file:
                                json.dump(v_data, file)
                    else:
                        self.update_checking_status = v_data["last_version"]

                except Exception as e:
                    logging.error(f"Could not check for updates. Error: {e}")
                    self.update_checking_status = None
            else:
                self.update_checking_status = None

            
            logging.info("PERS_CONFIG: Initialization successful.")
        except Exception as e:
            logging.error(f"PERS_CONFIG: Initialization error: {e}")
            self.update_checking_status="PASS"
            pass  
        
        self.faker_core=SXSCLI_Faker()
        logging.info(f"Initialization of the Faker core is successful. CORE VERSION: {self.faker_core.sxscli_version()}") 
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
            "id":"0",
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
        print(self.logo_color + self.logo)
        print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
        self.end_start_time_deb = time.time()
        logging.info(f"CLI: Initialization successful. Time taken: {self.end_start_time_deb - self.start_start_time_deb:.2f} seconds")

        if self.checking_for_updates and self.app_version != self.update_checking_status:
            if self.warnings:
                print(Fore.YELLOW + " New version available: " + f"{self.app_version} -> "+self.update_checking_status)

        logging.info("CLI: Successfully launched.")

        if any(value == "x" for value in [self.user_cfg["fullname"], self.user_cfg["nickname"], self.user_cfg["mail"]]):
            print(self.startmenu_color + "")
            print(Fore.WHITE + "Registration in the application: ")

            if not SXServiseCLI.check_internet(self):
                print(Fore.RED + "WARNING! No internet connection. Some functions may not work.")

            full_name = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Enter your full name:", default="John Doe")
            nickname = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Enter your nickname:", default="John")
            email = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Enter your email:", default="example@example.com")
            password = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Enter your password:", password=True)
            np = Prompt.ask(Fore.WHITE + " - SXSCLI_AUTH: Would you like to ask for your password at startup? (Y/N):", default="Y")

            need_password = np.lower() == "y"
            print("""
            Agreement to terms:
 - Copyright: https://www.sxcomp.42web.io/p/SXServiseCLI/copyright.txt
 - Support Policy: https://www.sxcomp.42web.io/p/SXServiseCLI/Support_Policy.txt
 - Terms of Use: https://www.sxcomp.42web.io/p/SXServiseCLI/Terms_of_Use.txt
 - Privacy Policy: https://www.sxcomp.42web.io/p/SXServiseCLI/Privacy_Policy.txt
 - Disclaimer of liability: https://www.sxcomp.42web.io/p/SXServiseCLI/Disclaimer_of_liability.txt
 - Acceptable Use Policy: https://www.sxcomp.42web.io/p/SXServiseCLI/Acceptable_Use_Policy.txt
 - I confirm that I am over 16 years old and I take full responsibility for my actions.
            """)

            agreement = input(Fore.WHITE + " - Y or N: ")
            if agreement.lower() in ["yes", "y"]:
                try:
                    result = firebase_client.register(email=email, password=password)
                    if result:
                        self.save_user_data(full_name, nickname, email, password, need_password)
                        print(Fore.GREEN + "Registration is successful!")
                        logging.info("CLI: Registration is successful.")
                        print(self.startmenu_color + " ")
                        SXServiseCLI.System.run_input(self)
                    else:
                        print(Fore.RED + "Registration failed!")
                        logging.warning("CLI: Registration failed!")
                        time.sleep(4)
                        sys.exit()
                except Exception as e:
                    print(Fore.RED + f"Error during registration: {str(e)}")
                    logging.error(f"CLI: Error during registration: {str(e)}")
                    sys.exit()
            else:
                print(Fore.RED + " -> You must agree to the terms to continue!")
                logging.warning("CLI: You must agree to the terms to continue!")
                time.sleep(4)
                sys.exit()

        elif self.user_cfg["need_password_"]:
            print(" ")
            if str(input(self.input_color + " - Enter password: ")) == self.user_cfg["password"]:
                print(" ")
                print(self.startmenu_color + f" Welcome, {self.user_cfg['nickname']}!")
                print(self.startmenu_color + " Do you need help? -> help")
                print(self.startmenu_color + " All you need in one place")
                print(" ")

                if not SXServiseCLI.check_internet(self) and self.warnings:
                    print(Fore.RED + "WARNING! No internet connection. Some functions may not work.")

                if SXServiseCLI.check_internet(self) and firebase_client.login(email=self.user_cfg["mail"], password=self.user_cfg["password"]):
                    logging.info("SXSCLI_L_C=Success")
                else:
                    logging.warning("SXSCLI_L_C=Error")
            else:
                print(self.errors_color + " -> Incorrect password try again later!")
                logging.warning("CLI: Incorrect password")
                time.sleep(4)
                sys.exit()

        else:
            if not SXServiseCLI.check_internet(self) and self.warnings:
                print(Fore.RED + "WARNING! No internet connection. Some functions may not work.")

            if SXServiseCLI.check_internet(self) and firebase_client.login(email=self.user_cfg["mail"], password=self.user_cfg["password"]):
                logging.info("SXSCLI_L_C=Success")
            else:
                logging.warning("SXSCLI_L_C=Error")

            print(self.startmenu_color + f" Welcome, {self.user_cfg['nickname']}!")
            print(self.startmenu_color + " Do you need help? -> help")
            print(self.startmenu_color + " All you need in one place")
            print(" ")
            SXServiseCLI.System.run_input(self)

    
    class System:
        def get_gpu_info(self):
            try:
                gpu_query = 'nvidia-smi --query-gpu=gpu_name,driver_version,memory.total,memory.free,memory.used,utilization.gpu,utilization.memory,temperature.gpu,cuda_version --format=csv,noheader,nounits'
                if platform.system() in ["Windows", "Linux"]:
                    try:
                        gpu_info = os.popen(gpu_query).read()
                    except Exception as e:
                        print(Fore.RED + f"Error fetching GPU info: {e}")
                        gpu_info = None
                else:
                    gpu_info = "GPU info not available for this system"
                    
                if gpu_info:
                    gpu_details = gpu_info.strip().split('\n')
                    for gpu in gpu_details:
                        try:
                            gpu_data = gpu.split(', ')
                            print(Fore.WHITE + f"""
        - GPU: {gpu_data[0]} 
        - Driver Version: {gpu_data[1]} 
        - Total Memory: {gpu_data[2]} MB 
        - Free Memory: {gpu_data[3]} MB 
        - Used Memory: {gpu_data[4]} MB 
        - GPU Utilization: {gpu_data[5]}% 
        - Memory Utilization: {gpu_data[6]}% 
        - GPU Temperature: {gpu_data[7]}°C 
        - CUDA Version: {gpu_data[8]}
                            """)
                        except Exception as e:
                            print(Fore.RED + f"Error processing GPU data: {e}")
                    try:
                        avg_gpu_utilization = sum([int(gpu_data[5].replace('%', '')) for gpu in gpu_details]) / len(gpu_details)
                        avg_memory_utilization = sum([int(gpu_data[6].replace('%', '')) for gpu in gpu_details]) / len(gpu_details)
                        print(Fore.WHITE + f"Average GPU Utilization: {avg_gpu_utilization}%")
                        print(Fore.WHITE + f"Average Memory Utilization: {avg_memory_utilization}%")
                    except Exception as e:
                        print(Fore.RED + f"Error calculating averages: {e}")
                else:
                    print(Fore.RED + "No GPU data available.")

                if platform.system() == "Linux":
                    try:
                        os.system("lspci | grep VGA")
                    except Exception as e:
                        print(Fore.RED + f"Error executing lspci: {e}")
                
                if platform.system() == "Linux":
                    try:
                        amd_info = os.popen('radeontop -l').read()
                        if amd_info:
                            print(Fore.WHITE + f"AMD GPU Support: {amd_info}")
                    except Exception as e:
                        print(Fore.RED + f"Error getting AMD GPU info: {e}")

                if platform.system() in ["Windows", "Linux"]:
                    try:
                        cuda_info = os.popen('nvcc --version').read()
                        if cuda_info:
                            print(Fore.CYAN + f"CUDA Info: {cuda_info.strip()}")
                    except Exception as e:
                        print(Fore.RED + f"Error getting CUDA info: {e}")

                if platform.system() == "Linux":
                    try:
                        opencl_info = os.popen('clinfo').read()
                        if opencl_info:
                            print(Fore.CYAN + "OpenCL Info:")
                            print(opencl_info)
                    except Exception as e:
                        print(Fore.RED + f"Error getting OpenCL info: {e}")

            except Exception as e:
                print(Fore.RED + f"Unexpected error: {e}")
                logging.error(f"System: Unexpected error: {e}")
            finally:
                print(" ")
                try:
                    SXServiseCLI.System.run_input(self)
                except Exception as e:
                    print(Fore.RED + f"Error running input: {e}")


        def get_cpu_info(self):
            try:
                cpu_percent = psutil.cpu_percent(interval=1)
                cpu_freq = psutil.cpu_freq()
                cpu_count_physical = psutil.cpu_count(logical=False)
                cpu_count_logical = psutil.cpu_count(logical=True)
                cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)
                cache = psutil.virtual_memory()
                print(Fore.WHITE+
f""" - System: {platform.system()} {platform.release()} - Machine: {platform.machine()}
 - Processor: {platform.processor()} 
 - Physical CPU cores: {cpu_count_physical} - Logical CPU cores: {cpu_count_logical}
 - Overall CPU usage: {cpu_percent}% - CPU usage per core: {cpu_per_core}
 - Min CPU frequency: {cpu_freq.min} MHz - Max CPU frequency: {cpu_freq.max} MHz
 - Total virtual memory: {cache.total / (1024**3):.2f} GB - Available virtual memory: {cache.available / (1024**3):.2f} GB
 - Used virtual memory: {cache.used / (1024**3):.2f} GB - Free virtual memory: {cache.free / (1024**3):.2f} GB
 - Memory usage: {cache.percent}% - Current CPU frequency: {cpu_freq.current} MHz """)
                
                try:
                    cpu_temp = psutil.sensors_temperatures()['coretemp'][0].current
                    print(Fore.WHITE+f"  - CPU temperature: {cpu_temp}°C")
                except (AttributeError, KeyError):
                    pass
                
                if platform.system() == "Linux":
                    os.system("lscpu")
                elif platform.system() == "Windows":
                    print(os.system("wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status"))
            except Exception as e:
                print(Fore.RED+f"Error: {e}")
                logging.error(f"System: Error: {e}")
            finally:
                print(" ")
                SXServiseCLI.System.run_input(self)
                
        def check_speed(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color + self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(" ")
            print(Fore.WHITE + " Welcome to SXSCLI:SpeedTest!")
            print(Fore.WHITE + " -> Please wait, the test is in progress...")
            print(" ")
            try:
                st = speedtest.Speedtest()
                st.get_best_server()
                download_speed = st.download() / 1_000_000 
                upload_speed = st.upload() / 1_000_000  
                ping = st.results.ping

                print(f" -> Download speed: {download_speed:.2f} Mbps")
                print(f" -> Upload speed: {upload_speed:.2f} Mbps")
                print(f" -> Latency (ping): {ping} ms")

            except Exception as e:
                logging.error(f"SpeedTest: Error: {e}")
                print(Fore.RED + f"Error: {e}")
            finally:
                print(" ")
                SXServiseCLI.System.run_input(self)

        class device:
            def format_bytes(self,size):
                for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                    if size < 1024:
                        return f"{size:.2f} {unit}"
                    size /= 1024
                return f"{size:.2f} TB"
            
            def start(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color + self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(" ")
                console=self.console
                
                try:
                    console.print(Panel("[bold cyan]System Information[/bold cyan]"))
                    console.print(f"[white]OS:[/white] {platform.system()} {platform.release()} {platform.version()} {platform.platform()}")
                    console.print(f"[white]Machine Name:[/white] {platform.node()}")
                    console.print(f"[white]Processor:[/white] {platform.processor()}")
                    console.print(f"[white]Architecture:[/white] {platform.architecture()}")
                    console.print(f"[white]Python Version:[/white] {platform.python_version()}")
                    console.print(f"[white]System Uptime:[/white] {psutil.boot_time()}")
                except Exception:
                    pass

                try:
                    console.print(Panel("[bold cyan]CPU Information[/bold cyan]"))
                    console.print(f"[white]CPU Cores (Physical):[/white] {psutil.cpu_count(logical=False)}")
                    console.print(f"[white]CPU Cores (Logical):[/white] {psutil.cpu_count(logical=True)}")
                    console.print(f"[white]CPU Frequency:[/white] {psutil.cpu_freq().current} MHz")
                    console.print(f"[white]CPU Usage:[/white] {psutil.cpu_percent(interval=1)}%")
                except Exception:
                    pass

                try:
                    mem = psutil.virtual_memory()
                    console.print(Panel("[bold cyan]Memory Information[/bold cyan]"))
                    console.print(f"[white]Total Memory:[/white] {SXServiseCLI.System.device.format_bytes(self,mem.total)}")
                    console.print(f"[white]Available Memory:[/white] {SXServiseCLI.System.device.format_bytes(self,mem.available)}")
                    console.print(f"[white]Used Memory:[/white] {SXServiseCLI.System.device.format_bytes(self,mem.used)}")
                    console.print(f"[white]Memory Usage:[/white] {mem.percent}%")
                except Exception:
                    pass

                try:
                    swap = psutil.swap_memory()
                    console.print(f"[white]Total Swap Memory:[/white] {SXServiseCLI.System.device.format_bytes(self,swap.total)}")
                    console.print(f"[white]Used Swap Memory:[/white] {SXServiseCLI.System.device.format_bytes(self,swap.used)}")
                    console.print(f"[white]Free Swap Memory:[/white] {SXServiseCLI.System.device.format_bytes(self,swap.free)}")
                    console.print(f"[white]Swap Usage:[/white] {swap.percent}%")
                except Exception:
                    pass

                try:
                    gpus = GPUtil.getGPUs()
                    if gpus:
                        console.print(Panel("[bold cyan]GPU Information[/bold cyan]"))
                        for gpu in gpus:
                            console.print(f"[white]GPU:[/white] {gpu.name}, [white]Load:[/white] {gpu.load * 100:.2f}%, [white]Temp:[/white] {gpu.temperature} °C, [white]VRAM Total:[/white] {gpu.memoryTotal} MB, [white]VRAM Used:[/white] {gpu.memoryUsed} MB")
                except Exception:
                    pass

                try:
                    if hasattr(psutil, "sensors_temperatures"):
                        console.print(Panel("[bold cyan]CPU Temperature[/bold cyan]"))
                        for name, entries in psutil.sensors_temperatures().items():
                            for entry in entries:
                                console.print(f"[white]{name}:[/white] {entry.label} - {entry.current} °C")
                except Exception:
                    pass

                try:
                    console.print(Panel("[bold cyan]Disk Information[/bold cyan]"))
                    for disk in psutil.disk_partitions():
                        usage = psutil.disk_usage(disk.mountpoint)
                        console.print(f"[white]Disk {disk.device} -[/white] Total: {SXServiseCLI.System.device.format_bytes(self,usage.total)}, Used: {SXServiseCLI.System.device.format_bytes(self,usage.used)}, Free: {SXServiseCLI.System.device.format_bytes(self,usage.free)}, Percent: {usage.percent}%")
                except Exception:
                    pass

                try:
                    console.print(Panel("[bold cyan]Network Information[/bold cyan]"))
                    net_io = psutil.net_io_counters()
                    console.print(f"[white]Bytes Sent:[/white] {SXServiseCLI.System.device.format_bytes(self,net_io.bytes_sent)}")
                    console.print(f"[white]Bytes Received:[/white] {SXServiseCLI.System.device.format_bytes(self,net_io.bytes_recv)}")
                except Exception:
                    pass

                try:
                    hostname = socket.gethostname()
                    local_ip = socket.gethostbyname(hostname)
                    console.print(f"[white]Hostname:[/white] {hostname}")
                    console.print(f"[white]Local IP Address:[/white] {local_ip}")
                    console.print(f"[white]MAC Address:[/white] {':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])}")
                except Exception:
                    pass

                try:
                    console.print(Panel("[bold cyan]Running Processes[/bold cyan]"))
                    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
                        try:
                            console.print(f"[white]PID:[/white] {proc.info['pid']}, [white]Name:[/white] {proc.info['name']}, [white]User:[/white] {proc.info['username']}, [white]CPU:[/white] {proc.info['cpu_percent']}%, [white]Memory:[/white] {SXServiseCLI.System.device.format_bytes(self,proc.info['memory_info'].rss)}")
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass
                except Exception:
                    pass
                
                try:
                    if hasattr(psutil, "sensors_battery"):
                        battery = psutil.sensors_battery()
                        if battery:
                            console.print(Panel("[bold cyan]Battery Information[/bold cyan]"))
                            console.print(f"[white]Battery Percent:[/white] {battery.percent}%")
                            console.print(f"[white]Plugged in:[/white] {'Yes' if battery.power_plugged else 'No'}")
                            console.print(f"[white]Time left:[/white] {battery.secsleft // 60} minutes")
                except Exception:
                    pass

                try:
                    console.print(Panel("[bold cyan]Logged in Users[/bold cyan]"))
                    for user in psutil.users():
                        console.print(f"[white]User:[/white] {user.name}, [white]Terminal:[/white] {user.terminal}, [white]Host:[/white] {user.host}, [white]Started:[/white] {user.started}")
                except Exception:
                    pass

                try:
                    console.print(Panel("[bold cyan]Audio Devices[/bold cyan]"))
                    import sounddevice as sd
                    audio_devices = sd.query_devices()
                    for device in audio_devices:
                        console.print(f"[white]Device:[/white] {device['name']}, [white]Max Input Channels:[/white] {device['max_input_channels']}, [white]Max Output Channels:[/white] {device['max_output_channels']}")
                except Exception:
                    pass

                try:
                    console.print(Panel("[bold cyan]Network Interfaces[/bold cyan]"))
                    interfaces = psutil.net_if_addrs()
                    for interface_name, interface_addresses in interfaces.items():
                        for addr in interface_addresses:
                            console.print(f"[white]Interface:[/white] {interface_name}, [white]Address:[/white] {addr.address}, [white]Family:[/white] {addr.family}, [white]Netmask:[/white] {addr.netmask}")
                except Exception:
                    pass

                try:
                    console.print(Panel("[bold cyan]User Accounts[/bold cyan]"))
                    users = psutil.users()
                    for user in users:
                        console.print(f"[white]User:[/white] {user.name}, [white]Terminal:[/white] {user.terminal}, [white]Host:[/white] {user.host}, [white]Started:[/white] {user.started}")
                except Exception:
                    pass

                try:
                    console.print(Panel("[bold cyan]System Boot Time[/bold cyan]"))
                    console.print(f"[white]System Boot Time:[/white] {psutil.boot_time()}")
                except Exception:
                    pass
                
                
                print(Fore.WHITE+"Thanks for using!")
                print(Fore.WHITE+"Powered by SXServiseCLI")
                print(" ")
                SXServiseCLI.System.run_input(self)
            
            def run(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color + self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(" ")
                print(Fore.WHITE + " Welcome to SXSCLI:Device!")
                print(" ")
                self.console.print(Panel("[bold cyan]Security Center[/bold cyan]"))
                print(Fore.WHITE + f"""
 This is the security center - a warning about dangerous actions.
 WARNING! This function is quite dangerous. You assume all responsibility for its use. 
 Sorry for the inconvenience, but unfortunately we have to ask you to agree to the terms before proceeding.

 - Start scanning - 1
 - Back - 0 or exit

 If you enter an incorrect value, you will automatically go to the main menu.
""")
                x = input(Fore.WHITE + " & >>> ")
                if x == "1":
                    SXServiseCLI.System.device.start(self)
                elif x == "0" or x.lower() == "exit":
                    SXServiseCLI.System.run_input(self)
                else:
                    SXServiseCLI.System.run_input(self)

                
        class AI:
            class mediapipe:
                def selfie_segmentation(self):
                    import cv2
                    import mediapipe as mp
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:MediaPipe:Selfie Segmentation!")
                    midiapipe_config_path = self.staff_path + "/mediapipe.json"
                    if os.path.exists(midiapipe_config_path):
                        with open(midiapipe_config_path, "r") as file:
                            mp_c = json.load(file)
                    else:
                        mp_c = {"selfie_segmentation": {"mirror": True, "cam": 0, "exit_button": "q"}}
                    logging.info(f"Loaded config: {mp_c}")
                    mirror = mp_c["selfie_segmentation"]["mirror"]
                    cam = mp_c["selfie_segmentation"]["cam"]
                    exit_button = mp_c["selfie_segmentation"]["exit_button"]
                    print(Fore.WHITE+"""
 MediaPipe Selfie Segmentation is a module within MediaPipe Solutions that uses a 
 pre-trained neural network to segment the subject from the background in images and video 
 streams, enabling real-time background removal and replacement.

 [0] Exit
 [1] Start
 [2] Settings
""")
                    try:
                        x=input(Fore.WHITE + " & >>> ")
                        if x == "0":
                            SXServiseCLI.System.run_input(self)
                        elif x == "1":
                            try:
                                mp_selfie_segmentation = mp.solutions.selfie_segmentation
                                selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)
                                mp_drawing = mp.solutions.drawing_utils
                                cap = cv2.VideoCapture(cam)
                                while cap.isOpened():
                                    ret, frame = cap.read()
                                    if not ret:
                                        break
                                    if mirror:
                                        frame = cv2.flip(frame, 1)
                                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                    results = selfie_segmentation.process(image)
                                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                                    condition = results.segmentation_mask > 0.5
                                    frame_bg = frame
                                    frame_fg = frame
                                    frame_fg = cv2.bitwise_and(frame_fg, frame_fg, mask=condition.astype('uint8'))
                                    frame_bg = cv2.bitwise_and(frame_bg, frame_bg, mask=(1 - condition).astype('uint8'))
                                    output_frame = cv2.add(frame_bg, frame_fg)
                                    cv2.imshow('SXSCLI: Selfie Segmentation (mediapipe)', output_frame)
                                    if cv2.waitKey(1) & 0xFF == ord(exit_button):
                                        logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                                        break
                            except KeyboardInterrupt:
                                logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                            except Exception as e:
                                logging.error(f"AI:MediaPipe:SelfieSegmentation: Error: {e}")
                            finally:
                                cap.release()
                                cv2.destroyAllWindows()
                                print(" ")
                                SXServiseCLI.System.run_input(self)
                        elif x == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(self.logo_color + self.logo + "\n")
                            cam = int(input(Fore.WHITE + f" - Enter camera index (default: {cam}): ") or cam)
                            mirror = input(Fore.WHITE + f" - Mirror image? (default: {mirror}): ").lower() == 'true' if input else mirror
                            exit_button = input(Fore.WHITE + f" - Exit button (default: {exit_button}): ") or exit_button
                            mp_c["selfie_segmentation"] = {"mirror": mirror, "cam": cam, "exit_button": exit_button}
                            with open(midiapipe_config_path, "w") as file:
                                json.dump(mp_c, file, indent=4)
                            print("  -> Settings saved.")
                            SXServiseCLI.System.run_input(self)
                        else:
                            SXServiseCLI.System.AI.mediapipe.error_inp(self)
                    except Exception as e:
                        SXServiseCLI.System.AI.mediapipe.error_log(self, e)
                
                def gesture_recognition(self):
                    import cv2
                    import mediapipe as mp
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:MediaPipe:Gesture Detection!")
                    midiapipe_config_path = self.staff_path + "/mediapipe.json"
                    if os.path.exists(midiapipe_config_path):
                        with open(midiapipe_config_path, "r") as file:
                            mp_c = json.load(file)
                    else:
                        mp_c = {"gesture_recognition": {"mirror": True, "cam": 0, "exit_button": "q"}}
                    logging.info(f"Loaded config: {mp_c}")
                    mirror = mp_c["gesture_recognition"]["mirror"]
                    cam = mp_c["gesture_recognition"]["cam"]
                    exit_button = mp_c["gesture_recognition"]["exit_button"]
                    print(Fore.WHITE+"""
 MediaPipe Gesture Detection is a module within MediaPipe Solutions that uses a 
 pre-trained neural network to recognize and track hand gestures in images and video 
 streams, enabling real-time gesture-based interaction.

 [0] Exit
 [1] Start
 [2] Settings
""")
                    try:
                        x=input(Fore.WHITE + " & >>> ")
                        if x == "0":
                            SXServiseCLI.System.run_input(self)
                        elif x == "1":
                            try:
                                mp_hands = mp.solutions.hands
                                hands = mp_hands.Hands(
                                    static_image_mode=False,
                                    max_num_hands=2,
                                    min_detection_confidence=0.5,
                                    min_tracking_confidence=0.5
                                )
                                mp_drawing = mp.solutions.drawing_utils
                                cap = cv2.VideoCapture(cam)
                                while cap.isOpened():
                                    ret, frame = cap.read()
                                    if not ret:
                                        break
                                    if mirror:
                                        frame = cv2.flip(frame, 1)
                                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                    results = hands.process(image)
                                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                                    if results.multi_hand_landmarks:
                                        for landmarks in results.multi_hand_landmarks:
                                            mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)
                                    cv2.imshow("SXSCLI: Gesture Detection (mediapipe)", image)
                                    if cv2.waitKey(1) & 0xFF == ord(exit_button):
                                        logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                                        break
                            except KeyboardInterrupt:
                                logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                            except Exception as e:
                                logging.error(f"AI:MediaPipe:GestureDetection: Error: {e}")
                            finally:
                                cap.release()
                                cv2.destroyAllWindows()
                                print(" ")
                                SXServiseCLI.System.run_input(self)
                        elif x == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(self.logo_color + self.logo + "\n")
                            cam = int(input(Fore.WHITE + f" - Enter camera index (default: {cam}): ") or cam)
                            mirror = input(Fore.WHITE + f" - Mirror image? (default: {mirror}): ").lower() == 'true' if input else mirror
                            exit_button = input(Fore.WHITE + f" - Exit button (default: {exit_button}): ") or exit_button
                            mp_c["gesture_detection"] = {"mirror": mirror, "cam": cam, "exit_button": exit_button}
                            with open(midiapipe_config_path, "w") as file:
                                json.dump(mp_c, file, indent=4)
                            print("  -> Settings saved.")
                            SXServiseCLI.System.run_input(self)
                        else:
                            SXServiseCLI.System.AI.mediapipe.error_inp(self)
                    except Exception as e:
                        SXServiseCLI.System.AI.mediapipe.error_log(self, e)
                
                def object_detection(self):
                    import cv2
                    import mediapipe as mp
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:MediaPipe:Object Detection!")
                    midiapipe_config_path = self.staff_path + "/mediapipe.json"
                    if os.path.exists(midiapipe_config_path):
                        with open(midiapipe_config_path, "r") as file:
                            mp_c = json.load(file)
                    else:
                        mp_c = {"object_detection": {"mirror": True, "cam": 0, "exit_button": "q", "model": "Shoe"}}
                    logging.info(f"Loaded config: {mp_c}")
                    mirror = mp_c["object_detection"]["mirror"]
                    cam = mp_c["object_detection"]["cam"]
                    exit_button = mp_c["object_detection"]["exit_button"]
                    model=mp_c["object_detection"]["model"]
                    print(Fore.WHITE+"""
 MediaPipe Object Detection is a module within MediaPipe Solutions that uses a 
 pre-trained neural network to detect and track objects in images and video streams, 
 providing real-time object recognition and localization.
 
 [0] Exit
 [1] Start
 [2] Settings
""")
                    try:
                        x=input(Fore.WHITE + " & >>> ")
                        if x == "0":
                            SXServiseCLI.System.run_input(self)
                        elif x == "1":
                            try:
                                mp_objectron = mp.solutions.objectron
                                objectron = mp_objectron.Objectron(
                                    static_image_mode=False,
                                    max_num_objects=5,
                                    model_name=model,
                                    min_detection_confidence=0.5,
                                    min_tracking_confidence=0.5
                                )
                                mp_drawing = mp.solutions.drawing_utils
                                cap = cv2.VideoCapture(cam)
                                while cap.isOpened():
                                    ret, frame = cap.read()
                                    if not ret:
                                        break
                                    if mirror:
                                        frame = cv2.flip(frame, 1)
                                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                    results = objectron.process(image)
                                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                                    if results.detected_objects:
                                        for detected_object in results.detected_objects:
                                            mp_drawing.draw_landmarks(image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
                                            mp_drawing.draw_axis(image, detected_object.rotation, detected_object.translation)
                                    cv2.imshow("SXSCLI: MediaPipe Objectron (mediapipe)", image)
                                    if cv2.waitKey(1) & 0xFF == ord(exit_button):
                                        logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                                        break
                            except KeyboardInterrupt:
                                logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                            except Exception as e:
                                logging.error(f"AI:MediaPipe:ObjectDetection: Error: {e}")
                            finally:
                                cap.release()
                                cv2.destroyAllWindows()
                                print(" ")
                                SXServiseCLI.System.run_input(self)
                        elif x == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(self.logo_color + self.logo + "\n")
                            cam = int(input(Fore.WHITE + f" - Enter camera index (default: {cam}): ") or cam)
                            mirror = input(Fore.WHITE + f" - Mirror image? (default: {mirror}): ").lower() == 'true' if input else mirror
                            exit_button = input(Fore.WHITE + f" - Exit button (default: {exit_button}): ") or exit_button
                            model = input(Fore.WHITE + f" - Model (default: {model}): ") or model
                            mp_c["object_detection"] = {"mirror": mirror, "cam": cam, "exit_button": exit_button, "model": model}
                            with open(midiapipe_config_path, "w") as file:
                                json.dump(mp_c, file, indent=4)
                            print("  -> Settings saved.")
                            SXServiseCLI.System.run_input(self)
                        else:
                            SXServiseCLI.System.AI.mediapipe.error_inp(self)
                    except Exception as e:
                        SXServiseCLI.System.AI.mediapipe.error_log(self, e)
                
                def holistic_detection(self):
                    import cv2
                    import mediapipe as mp
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:MediaPipe:Holistic Detection!")
                    midiapipe_config_path = self.staff_path + "/mediapipe.json"
                    if os.path.exists(midiapipe_config_path):
                        with open(midiapipe_config_path, "r") as file:
                            mp_c = json.load(file)
                    else:
                        mp_c = {"holistic_detection": {"mirror": True, "cam": 0, "exit_button": "q"}}
                    logging.info(f"Loaded config: {mp_c}")
                    mirror = mp_c["holistic_detection"]["mirror"]
                    cam = mp_c["holistic_detection"]["cam"]
                    exit_button = mp_c["holistic_detection"]["exit_button"]
                    print(Fore.WHITE+"""
 MediaPipe Holistic is a module within MediaPipe Solutions that uses a
 pre-trained neural network to detect and track full-body landmarks, including 
 face, hands, and pose, in images and video streams, providing comprehensive human 
 motion tracking.

 [0] Exit
 [1] Start
 [2] Settings
""")
                    try:
                        x=input(Fore.WHITE + " & >>> ")
                        if x == "0":
                            SXServiseCLI.System.run_input(self)
                        elif x == "1":
                            print(Fore.WHITE + f" -> Using camera index: {cam}: APP: Holistic Detection")
                            print(Fore.WHITE + f" -> Press '{exit_button}' to exit the program.\n")
                            try:
                                mp_holistic = mp.solutions.holistic
                                mp_drawing = mp.solutions.drawing_utils
                                cap = cv2.VideoCapture(cam)
                                with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
                                    while cap.isOpened():
                                        ret, frame = cap.read()
                                        if not ret:
                                            break
                                        if mirror:
                                            frame = cv2.flip(frame, 1)
                                        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                        results = holistic.process(image)
                                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                                        if results.face_landmarks:
                                            mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)
                                        if results.left_hand_landmarks:
                                            mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                                        if results.right_hand_landmarks:
                                            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                                        if results.pose_landmarks:
                                            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
                                        cv2.imshow('SXSCLI: Holistic Detection (mediapipe)', image)
                                        if cv2.waitKey(1) & 0xFF == ord(exit_button):
                                            logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                                            break
                            except KeyboardInterrupt:
                                logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                            except Exception as e:
                                logging.error(f"AI:MediaPipe:HolisticDetection: Error: {e}")
                            finally:
                                cap.release()
                                cv2.destroyAllWindows()
                                print(" ")
                                SXServiseCLI.System.run_input(self)
                        elif x == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(self.logo_color + self.logo + "\n")
                            cam = int(input(Fore.WHITE + f" - Enter camera index (default: {cam}): ") or cam)
                            mirror = input(Fore.WHITE + f" - Mirror image? (default: {mirror}): ").lower() == 'true' if input else mirror
                            exit_button = input(Fore.WHITE + f" - Exit button (default: {exit_button}): ") or exit_button
                            mp_c["holistic_detection"] = {"mirror": mirror, "cam": cam, "exit_button": exit_button}
                            with open(midiapipe_config_path, "w") as file:
                                json.dump(mp_c, file, indent=4)
                            print("  -> Settings saved.")
                            SXServiseCLI.System.run_input(self)
                        else:
                            SXServiseCLI.System.AI.mediapipe.error_inp(self)
                    except Exception as e:
                        SXServiseCLI.System.AI.mediapipe.error_log(self, e)
                
                def hand_tracking(self):
                    import cv2
                    import mediapipe as mp
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:MediaPipe:Hand Tracking!")
                    midiapipe_config_path = self.staff_path + "/mediapipe.json"
                    if os.path.exists(midiapipe_config_path):
                        with open(midiapipe_config_path, "r") as file:
                            mp_c = json.load(file)
                    else:
                        mp_c = {"hand_tracking": {"mirror": True, "cam": 0, "exit_button": "q"}}
                    logging.info(f"Loaded config: {mp_c}")
                    mirror = mp_c["hand_tracking"]["mirror"]
                    cam = mp_c["hand_tracking"]["cam"]
                    exit_button = mp_c["hand_tracking"]["exit_button"]
                    print(Fore.WHITE+"""
 MediaPipe Hand Tracking is a module within MediaPipe Solutions that 
 uses a pre-trained neural network to detect and track key hand landmarks in 
 images and video streams, providing highly accurate tracking of hand movements.

 [0] Exit
 [1] Start
 [2] Settings
""")
                    try:
                        x=input(Fore.WHITE + " & >>> ")
                        if x == "0":
                            SXServiseCLI.System.run_input(self)
                        elif x == "1":
                            print(Fore.WHITE + f" -> Using camera index: {cam}: APP: Hand Tracking")
                            print(Fore.WHITE + f" -> Press '{exit_button}' to exit the program.\n")
                            try:
                                mp_hands = mp.solutions.hands
                                hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
                                mp_drawing = mp.solutions.drawing_utils
                                cap = cv2.VideoCapture(cam)
                                while cap.isOpened():
                                    ret, frame = cap.read()
                                    if not ret:
                                        break
                                    if mirror: 
                                        frame = cv2.flip(frame, 1)
                                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                    results = hands.process(image)
                                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                                    if results.multi_hand_landmarks:
                                        for hand_landmarks in results.multi_hand_landmarks:
                                            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                                    cv2.imshow('SXSCLI: Hand Tracking (mediapipe)', image)
                                    if cv2.waitKey(1) & 0xFF == ord(exit_button):
                                        logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                                        break
                            except KeyboardInterrupt:
                                logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                            except Exception as e:
                                logging.error(f"AI:MediaPipe:HandTracking: Error: {e}")
                            finally:
                                cap.release()
                                cv2.destroyAllWindows()
                                print(" ")
                                SXServiseCLI.System.run_input(self)
                        elif x == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(self.logo_color + self.logo + "\n")
                            cam = int(input(Fore.WHITE + f" - Enter camera index (default: {cam}): ") or cam)
                            mirror = input(Fore.WHITE + f" - Mirror image? (default: {mirror}): ").lower() == 'true' if input else mirror
                            exit_button = input(Fore.WHITE + f" - Exit button (default: {exit_button}): ") or exit_button
                            mp_c["hand_tracking"] = {"mirror": mirror, "cam": cam, "exit_button": exit_button}
                            with open(midiapipe_config_path, "w") as file:
                                json.dump(mp_c, file, indent=4)
                            print("  -> Settings saved.")
                            SXServiseCLI.System.run_input(self)
                        else:
                            SXServiseCLI.System.AI.mediapipe.error_inp(self)
                    except Exception as e:
                        SXServiseCLI.System.AI.mediapipe.error_log(self, e)
                
                def pose_detection(self):
                    import cv2
                    import mediapipe as mp
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:MediaPipe:Pose Detection!")
                    midiapipe_config_path = self.staff_path + "/mediapipe.json"
                    if os.path.exists(midiapipe_config_path):
                        with open(midiapipe_config_path, "r") as file:
                            mp_c = json.load(file)
                    else:
                        mp_c = {"pose_detection": {"mirror": True, "cam": 0, "exit_button": "q"}}
                    logging.info(f"Loaded config: {mp_c}")
                    mirror = mp_c["pose_detection"]["mirror"]
                    cam = mp_c["pose_detection"]["cam"]
                    exit_button = mp_c["pose_detection"]["exit_button"]
                    print(Fore.WHITE+"""
 MediaPipe Pose Detection is a module within MediaPipe Solutions that 
 uses a pre-trained neural network to detect and track key body landmarks 
 in images and video streams, providing highly detailed body pose mapping.
            
 [0] Exit
 [1] Start
 [2] Settings
""")
                    try:
                        x=input(Fore.WHITE + " & >>> ")
                        if x == "0":
                            SXServiseCLI.System.run_input(self)
                        elif x == "1":
                            print(Fore.WHITE + f" -> Using camera index: {cam}: APP: Pose Detection")
                            print(Fore.WHITE + f" -> Press '{exit_button}' to exit the program.\n")
                            try:
                                mp_pose = mp.solutions.pose
                                pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
                                mp_drawing = mp.solutions.drawing_utils
                                cap = cv2.VideoCapture(cam)
                                while cap.isOpened():
                                    ret, frame = cap.read()
                                    if not ret:
                                        break
                                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                    results = pose.process(image)
                                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                                    if results.pose_landmarks:
                                        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                                    cv2.imshow('SXSCLI: Pose Detection (mediapipe)', image)
                                    if cv2.waitKey(1) & 0xFF == ord(exit_button):
                                        logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                                        break
                            except KeyboardInterrupt:
                                logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                            except Exception as e:
                                logging.error(f"AI:MediaPipe:PoseDetection: Error: {e}")
                            finally:
                                cap.release()
                                cv2.destroyAllWindows()
                                print(" ")
                                SXServiseCLI.System.run_input(self)
                        elif x == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(self.logo_color + self.logo + "\n")
                            cam = int(input(Fore.WHITE + f" - Enter camera index (default: {cam}): ") or cam)
                            mirror = input(Fore.WHITE + f" - Mirror image? (default: {mirror}): ").lower() == 'true' if input else mirror
                            exit_button = input(Fore.WHITE + f" - Exit button (default: {exit_button}): ") or exit_button
                            mp_c["pose_detection"] = {"mirror": mirror, "cam": cam, "exit_button": exit_button}
                            with open(midiapipe_config_path, "w") as file:
                                json.dump(mp_c, file, indent=4)
                            print("  -> Settings saved.")
                            SXServiseCLI.System.run_input(self)
                        else:
                            SXServiseCLI.System.AI.mediapipe.error_inp(self)
                    except Exception as e:
                        SXServiseCLI.System.AI.mediapipe.error_log(self, e)
                                
                def face_mesh(self):
                    import cv2
                    import mediapipe as mp
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:MediaPipe:Face Mesh!")
                    midiapipe_config_path = self.staff_path + "/mediapipe.json"
                    if os.path.exists(midiapipe_config_path):
                        with open(midiapipe_config_path, "r") as file:
                            mp_c = json.load(file)
                    else:
                        mp_c = {"face_mesh": {"mirror": True, "cam": 0, "exit_button": "q"}}
                    logging.info(f"Loaded config: {mp_c}")
                    mirror = mp_c["face_mesh"]["mirror"]
                    cam = mp_c["face_mesh"]["cam"]
                    exit_button = mp_c["face_mesh"]["exit_button"]
                    print("""
 MediaPipe Face Mesh is a module within MediaPipe Solutions that 
 uses a pre-trained neural network to detect and track 468 facial landmarks 
 in images and video streams, providing highly detailed face mapping.
            
 [0] Exit
 [1] Start
 [2] Settings
""")
                    try:
                        x=input(Fore.WHITE + " & >>> ")
                        if x == "0":
                            SXServiseCLI.System.run_input(self)
                        elif x == "1":
                            print(Fore.WHITE + f" -> Using camera index: {cam}: APP: Face Mesh")
                            print(Fore.WHITE + f" -> Press '{exit_button}' to exit the program.\n")
                            try:
                                cap = cv2.VideoCapture(cam)
                                mp_face_mesh = mp.solutions.face_mesh.FaceMesh()
                                while cap.isOpened():
                                    ret, frame = cap.read()
                                    if not ret: break
                                    if mirror: frame = cv2.flip(frame, 1)
                                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                    results = mp_face_mesh.process(rgb_frame)
                                    if results.multi_face_landmarks:
                                        for landmarks in results.multi_face_landmarks:
                                            for idx, landmark in enumerate(landmarks.landmark):
                                                h, w, _ = frame.shape
                                                x, y = int(landmark.x * w), int(landmark.y * h)
                                                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                                    cv2.imshow("SXSCLI: Face Mesh (mediapipe)", frame)
                                    if cv2.waitKey(1) & 0xFF == ord(exit_button): 
                                        logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                                        break
                            except KeyboardInterrupt:
                                logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                            except Exception as e:
                                logging.error(f"AI:MediaPipe:FaceMesh: Error: {e}")
                            finally:
                                cap.release()
                                cv2.destroyAllWindows()
                                print(" ")
                                SXServiseCLI.System.run_input(self)
                        elif x == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(self.logo_color + self.logo + "\n")
                            cam = int(input(Fore.WHITE + f" - Enter camera index (default: {cam}): ") or cam)
                            mirror = input(Fore.WHITE + f" - Mirror image? (default: {mirror}): ").lower() == 'true' if input else mirror
                            exit_button = input(Fore.WHITE + f" - Exit button (default: {exit_button}): ") or exit_button
                            mp_c["face_detection"] = {"mirror": mirror, "cam": cam, "exit_button": exit_button}
                            with open(midiapipe_config_path, "w") as file:
                                json.dump(mp_c, file, indent=4)
                            print("  -> Settings saved.")
                            SXServiseCLI.System.run_input(self)
                        else:
                            SXServiseCLI.System.AI.mediapipe.error_inp(self)
                    except Exception as e:
                        SXServiseCLI.System.AI.mediapipe.error_log(self, e)
                
                def face_detection(self):
                    import cv2
                    import mediapipe as mp
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:MediaPipe:Face Detection!")
                    midiapipe_config_path = self.staff_path + "/mediapipe.json"
                    if os.path.exists(midiapipe_config_path):
                        with open(midiapipe_config_path, "r") as file:
                            mp_c = json.load(file)
                    else:
                        mp_c = {"face_detection": {"mirror": True, "cam": 0, "exit_button": "q"}}
                    logging.info(f"Loaded config: {mp_c}")
                    mirror = mp_c["face_detection"]["mirror"]
                    cam = mp_c["face_detection"]["cam"]
                    exit_button = mp_c["face_detection"]["exit_button"]

                    print("""
 MediaPipe Face Detection is a module within MediaPipe Solutions that 
 uses a pre-trained neural network to detect faces in images and video streams.
            
 [0] Exit
 [1] Start
 [2] Settings
            """)
                    try:
                        x = input(Fore.WHITE + " & >>> ")
                        if x == "0":
                            SXServiseCLI.System.run_input()
                        elif x == "1":
                            print(Fore.WHITE + f" -> Using camera index: {cam}: APP: Face Detection")
                            print(Fore.WHITE + f" -> Press '{exit_button}' to exit the program.\n")
                            try:
                                cap = cv2.VideoCapture(cam)
                                mp_face = mp.solutions.face_detection.FaceDetection()
                                while cap.isOpened():
                                    ret, frame = cap.read()
                                    if not ret: break
                                    if mirror: frame = cv2.flip(frame, 1)
                                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                    results = mp_face.process(rgb_frame)
                                    if results.detections:
                                        for detection in results.detections:
                                            bbox = detection.location_data.relative_bounding_box
                                            h, w, _ = frame.shape
                                            x, y, w_box, h_box = int(bbox.xmin * w), int(bbox.ymin * h), int(bbox.width * w), int(bbox.height * h)
                                            cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
                                    cv2.imshow("SXSCLI: Face Detection (mediapipe)", frame)
                                    if cv2.waitKey(1) & 0xFF == ord(exit_button): 
                                        logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                                        break
                            except KeyboardInterrupt:
                                logging.info("AI:MediaPipe:SelfieSegmentation: Stopped by user.")
                            except Exception as e:
                                logging.error(f"AI:MediaPipe:FaceDetection: Error: {e}")
                            finally:
                                cap.release()
                                cv2.destroyAllWindows()
                                print(" ")
                                SXServiseCLI.System.run_input(self)
                        elif x == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(self.logo_color + self.logo + "\n")
                            cam = int(input(Fore.WHITE + f" - Enter camera index (default: {cam}): ") or cam)
                            mirror = input(Fore.WHITE + f" - Mirror image? (default: {mirror}): ").lower() == 'true' if input else mirror
                            exit_button = input(Fore.WHITE + f" - Exit button (default: {exit_button}): ") or exit_button
                            mp_c["face_detection"] = {"mirror": mirror, "cam": cam, "exit_button": exit_button}
                            with open(midiapipe_config_path, "w") as file:
                                json.dump(mp_c, file, indent=4)
                            print("  -> Settings saved.")
                            SXServiseCLI.System.run_input(self)
                        else:
                            SXServiseCLI.System.AI.mediapipe.error_inp(self)
                    except Exception as e:
                        SXServiseCLI.System.AI.mediapipe.error_log(self, e)
                
                def error_inp(self):
                    print(Fore.RED + " -> Invalid input. Please try again.")
                    SXServiseCLI.System.AI.mediapipe.run_input(self)
                
                def error_log(self, e):
                    print(Fore.RED + f"Error: {e}")
                    logging.error(f"AI:MediaPipe: Error: {e}")
                    SXServiseCLI.System.run_input(self)
                
                def process_input(self, input_c):
                    try:
                        options = {
                            0: SXServiseCLI.System.run_input,
                            1: SXServiseCLI.System.AI.mediapipe.face_detection,
                            2: SXServiseCLI.System.AI.mediapipe.face_mesh,
                            3: SXServiseCLI.System.AI.mediapipe.pose_detection,
                            4: SXServiseCLI.System.AI.mediapipe.hand_tracking,
                            5: SXServiseCLI.System.AI.mediapipe.holistic_detection,
                            6: SXServiseCLI.System.AI.mediapipe.object_detection,
                            7: SXServiseCLI.System.AI.mediapipe.gesture_recognition,
                            8: SXServiseCLI.System.AI.mediapipe.selfie_segmentation,
                        }

                        try:
                            func = options.get(int(input_c), None)
                            if func:
                                func(self)
                            else:
                                print(Fore.RED + " -> Invalid input. Please try again.")
                                SXServiseCLI.System.AI.mediapipe.run_input(self)
                        except ValueError:
                            print(Fore.RED + " -> Invalid input. Please enter a number.")
                            SXServiseCLI.System.AI.mediapipe.run_input(self)
                    except Exception as e:
                        logging.error(f"AI:MediaPipe: Error processing input: {e}")
                        SXServiseCLI.System.run_input(self)
                
                def run_input(self):
                    SXServiseCLI.System.AI.mediapipe.process_input(self, input_c=input(Fore.WHITE + " & >>> "))
                
                def run(self):
                    midiapipe_config_path = self.staff_path + "/mediapipe.json"
                    if not os.path.exists(midiapipe_config_path):
                        data = {
"face_detection": {
    "mirror": True,
    "cam": 0,
    "exit_button": "q"
},
"face_mesh": {
    "mirror": True,
    "cam": 0,
    "exit_button": "q"
},
"pose_detection": {
    "mirror": True,
    "cam": 0,
    "exit_button": "q"
},
"hand_tracking": {
    "mirror": True,
    "cam": 0,
    "exit_button": "q"
},
"holistic_detection": {
    "mirror": True,
    "cam": 0,
    "exit_button": "q"
},
"object_detection": {
    "mirror": True,
    "cam": 0,
    "exit_button": "q",
    "model": "Shoe"
},
"gesture_recognition": {
    "mirror": True,
    "cam": 0,
    "exit_button": "q"
},
"selfie_segmentation": {
    "mirror": True,
    "cam": 0,
    "exit_button": "q"
},
                        }
                        with open(midiapipe_config_path, "w") as file:
                            json.dump(data, file, indent=4)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:MEDIAPIPE!")
                    print("""
 MediaPipe Solutions provides a set of libraries and tools that allow 
 you to quickly apply artificial intelligence (AI) and machine learning (ML) 
 techniques to your applications.
 
 [0] Exit               [3] Pose Detection         [6] Object Detection 
 [1] Face Detection     [4] Hand Tracking          [7] Gesture Recognition
 [2] Face Mesh          [5] Holistic Detection     [8] Selfie Segmentation

""")
                    SXServiseCLI.System.AI.mediapipe.run_input(self)
                    
            class genai_google:
                def start_chat(self):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:GENAI:Chat!")
                    console=self.console
                    with open(self.staff_path + "/genai.json", "r") as file:
                        genai_data = json.load(file)
                    print(Fore.WHITE + " -> To exit, say: exit")
                    print(" ")
                    try:
                        print(Fore.GREEN + f"-> Connected to: {genai_data['api_key']} ({genai_data['model']})")
                        console.print(Panel("[bold cyan]GEMINI[/bold cyan]"))
                        print(" ")
                        sxscli = SXSCLI_GENAI()
                        settings_json = json.dumps({
                            "model": genai_data['model'],
                            "api_key": genai_data['api_key'],
                            "temperature": 0.7,
                            "max_tokens": 100,
                            "type": "chat",
                            "save_history": True,
                            "personalized_responses": True,
                            "user_name": self.user_cfg["nickname"],
                            "full_name": self.user_cfg["fullname"]
                        })
                        sxscli.System(sxscli).config(settings_json)
                        sxscli.start_chat()
                        while True:
                            user_input = input(Fore.LIGHTWHITE_EX + "You: ")
                            if user_input.lower() == "exit":
                                SXServiseCLI.System.run_input(self)
                            response = sxscli.send_message(user_input)
                            print(Fore.CYAN + f"AI: {response.text}")
                    
                    except Exception as e:
                        print(Fore.RED + f"Error starting chat: {e}")
                        logging.error(f"Component GENAI: Error starting chat: {e}")
                        SXServiseCLI.System.run_input(self)

                def cs_chat(self):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:GENAI:New Settings!")
                    m_model = Prompt.ask(Fore.WHITE + " - Enter model:", default=self.genai_def_settings["model"])
                    m_api_key = Prompt.ask(Fore.WHITE + " - Enter API Key:")
                    m_temp = Prompt.ask(Fore.WHITE + " - Enter temperature:", default=str(self.genai_def_settings["temperature"]))
                    m_max_tokens = Prompt.ask(Fore.WHITE + " - Enter max tokens:", default=str(self.genai_def_settings["max_tokens"]))

                    genai_data = {
                        "model": m_model,
                        "api_key": m_api_key,
                        "temperature": float(m_temp),
                        "max_tokens": int(m_max_tokens)
                    }

                    with open(self.staff_path + "/genai.json", "w") as file:
                        json.dump(genai_data, file)

                    print(Fore.GREEN + "Settings updated successfully!")
                    SXServiseCLI.System.run_input(self)

                def settings_chat(self):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:GENAI:Settings!")
                    console=self.console
                    with open(self.staff_path + "/genai.json", "r") as file:
                        genai_data = json.load(file)
                    console.print(Panel("[bold cyan]Gemini settings[/bold cyan]"))
                    print(" ")
                    print(Fore.WHITE + 
f"""
 GenAI, or Generative Artificial Intelligence, represents a new generation of 
 intelligent systems capable of generating diverse types of content. From text 
 and images to music and video, it leverages advanced algorithms and neural 
 networks to create high-quality, innovative outputs.

 Information about the model:
  - Model: {genai_data["model"]}
  - API Key: {genai_data["api_key"]}
  - Temperature: {genai_data["temperature"]}
  - Max Tokens: {genai_data["max_tokens"]}

 Additional Functions:
  - Currently, no additional content is available.

 Commands:
  - Change settings → cs
  - Back to previous menu → exit
""")

                    action = input(Fore.BLUE + " GENAI >>> ").strip().lower()
                    if action == "cs":
                        SXServiseCLI.System.AI.genai_google.cs_chat(self)
                    elif action == "exit":
                        SXServiseCLI.System.run_input(self)
                    else:
                        print(Fore.RED + " -> Incorrect command")
                        logging.error("Component GENAI: Incorrect command")
                        SXServiseCLI.System.run_input(self)

                def run(self):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color + self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print(Fore.WHITE + " Welcome to SXSCLI:AI:GENAI!")

                    filename = self.staff_path + "/genai.json"
                    genai_data = {
                        "model": self.genai_def_settings["model"],
                        "api_key": "x",
                        "temperature": self.genai_def_settings["temperature"],
                        "max_tokens": self.genai_def_settings["max_tokens"]
                    }
                    
                    if not os.path.isfile(filename):
                        with open(filename, "w") as file:
                            json.dump(genai_data, file)
                            
                    logging.info("Component GENAI: Successfully launched.")
                    print(Fore.CYAN + "══════════════════════════════════════════════════════════════════════════════")
                    print(Fore.WHITE + "                           GenAI: Generative AI                              ")
                    print(Fore.CYAN + "══════════════════════════════════════════════════════════════════════════════")
                    print(Fore.WHITE + """
 GenAI, or Generative Artificial Intelligence, represents a cutting-edge 
 generation of intelligent systems that leverage complex algorithms and 
 neural networks to generate diverse types of content. From crafting 
 engaging text and stunning visuals to producing music and videos, GenAI 
 is revolutionizing the way creativity meets technology.

 With the power of advanced machine learning models, GenAI can assist 
 in generating high-quality content, automating tasks, and providing 
 creative solutions to various industries, including entertainment, 
 marketing, design, and more.

 Core Features:
   - Text Generation: Generate human-like text for various applications.
   - Image Generation: Create stunning visuals and artwork.
   - Music Composition: Compose original music tailored to your needs.
   - Video Creation: Produce high-quality videos from scratch.

 Available Commands: (BETA)
   - Start a chat  → start  : Begin an interactive conversation with GenAI.
   - Settings      → st    : Customize your experience with GenAI.
   - Exit          → exit  : Exit the GenAI interface.

 Join the next wave of artificial intelligence innovation with GenAI, and 
 unleash your creative potential with the help of advanced technology.
""")


                    action = input(Fore.BLUE + " >>> ").strip().lower()
                    if action == "start":
                        SXServiseCLI.System.AI.genai_google.start_chat(self)
                    elif action == "st":
                        SXServiseCLI.System.AI.genai_google.settings_chat(self)
                    elif action == "exit":
                        SXServiseCLI.System.run_input(self)
                    else:
                        print(Fore.RED + "Invalid command.")
                        logging.error("Component GENAI: Invalid command.")
                        SXServiseCLI.System.run_input(self)
                        
        def pers(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color + self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(" ")
            console=self.console
            console.print(Panel("[bold cyan]Personalization[/bold cyan]"))
            print(f"""
Personalization Settings:
  - Logo Color:        {Fore.WHITE + self.pers_cfg["CLI"]["logo_color"]}
  - Input Color:       {Fore.WHITE + self.pers_cfg["CLI"]["input_color"]}
  - Errors Color:      {Fore.WHITE + self.pers_cfg["CLI"]["errors_color"]}
  - Start Menu Color:  {Fore.WHITE + self.pers_cfg["CLI"]["start_menu_color"]}
  - Show Version:      {str(Fore.WHITE + str(self.pers_cfg["CLI"]["show_version"]))}

Available Actions:
  - Change Colors:     custom -r -colors
  - Change Other:      custom -r -other
  - Return to Menu:    return
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
            console=self.console
            print(Fore.WHITE + " Welcome to SXSCLI:CONFIG!")
            logging.info("Component CONFIG: Successfully launched.")
            console.print(Panel("[bold cyan]Config[/bold cyan]"))
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
                    console=self.console
                    result_path_whois = f"Staff/results/{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}_portcan_result.log"
                    os.makedirs(os.path.dirname(result_path_whois), exist_ok=True)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    console.print(Panel("[bold cyan]Portscan[/bold cyan]"))
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
                        console=self.console
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(self.logo_color + self.logo)
                        print(" ")
                        console.print(Panel("[bold cyan]WHOIS[/bold cyan]"))
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
                            print(Fore.WHITE + "\nDNS Servers:")
                            dns_servers = dns.resolver.resolve(domain, 'NS')
                            for ns in dns_servers:
                                print(Fore.WHITE + f" - DNS Server: {ns.target}")
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - DNS Server: {ns.target}\n")
                                result_file.flush()
                        except Exception as e:
                            logging.error(f"Component WHOIS: DNS Server error: {e}")
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component WHOIS: DNS Server error: {e}\n")
                            result_file.flush()
                            print(self.errors_color + f"DNS Server error: {e}")
                        
                        try:
                            print(Fore.WHITE + "\nServer Info:")
                            response = requests.head(f"https://{domain}")
                            
                            server_info = response.headers.get('Server')
                            if server_info:
                                print(Fore.WHITE + f" - Server: {server_info}")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Server: {server_info}\n")
                                    result_file.flush()
                            else:
                                print(Fore.YELLOW + " - Server info not found.")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Server info not found.\n")
                                    result_file.flush()
                        except Exception as e:
                            logging.error(f"Component Server Info: Error fetching server details: {e}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component Server Info: Error fetching server details: {e}\n")
                                result_file.flush()
                            print(Fore.RED + f"Error fetching server details: {e}")
                        
                        try:
                            print(Fore.WHITE + "\nIPv6 Address:")
                            ipv6_records = dns.resolver.resolve(domain, 'AAAA')
                            for ipv6 in ipv6_records:
                                print(Fore.WHITE + f" - IPv6 Address: {ipv6}")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - IPv6 Address: {ipv6}\n")
                                    result_file.flush()
                        except Exception as e:
                            logging.error(f"Component IPv6 Lookup: Error fetching IPv6 records: {e}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component IPv6 Lookup: Error fetching IPv6 records: {e}\n")
                                result_file.flush()
                            print(Fore.RED + f"Error fetching IPv6 records: {e}")

                        try:
                            print(Fore.WHITE + "\nHTTP Security Headers:")
                            response = requests.head(f"https://{domain}")
                            security_headers = {
                                "Strict-Transport-Security": response.headers.get('Strict-Transport-Security'),
                                "Content-Security-Policy": response.headers.get('Content-Security-Policy'),
                                "X-Content-Type-Options": response.headers.get('X-Content-Type-Options'),
                            }
                            for header, value in security_headers.items():
                                if value:
                                    print(Fore.WHITE + f" - {header}: {value}")
                                    with open('result_file.txt', 'a') as result_file:
                                        result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - {header}: {value}\n")
                                        result_file.flush()
                                else:
                                    print(Fore.YELLOW + f" - {header}: Not found")
                                    with open('result_file.txt', 'a') as result_file:
                                        result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - {header}: Not found\n")
                                        result_file.flush()
                        except Exception as e:
                            logging.error(f"Component HTTP Headers: Error fetching security headers: {e}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component HTTP Headers: Error fetching security headers: {e}\n")
                                result_file.flush()
                            print(Fore.RED + f"Error fetching security headers: {e}")
                        
                        try:
                            print(Fore.WHITE + "\nDNSSEC Support:")
                            dnssec_records = dns.resolver.resolve(domain, 'DNSKEY')
                            if dnssec_records:
                                print(Fore.WHITE + " - DNSSEC is enabled.")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - DNSSEC is enabled.\n")
                                    result_file.flush()
                            else:
                                print(Fore.YELLOW + " - DNSSEC is not enabled.")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - DNSSEC is not enabled.\n")
                                    result_file.flush()
                        except Exception as e:
                            logging.error(f"Component DNSSEC: Error fetching DNSSEC data: {e}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component DNSSEC: Error fetching DNSSEC data: {e}\n")
                                result_file.flush()
                            print(Fore.RED + f"Error fetching DNSSEC data: {e}")

                        try:
                            print(Fore.WHITE + "\nSubdomains:")
                            subdomains_api = f"https://api.subdomainfinder.io/{domain}"
                            response = requests.get(subdomains_api)
                            subdomains = response.json().get("subdomains", [])
                            if subdomains:
                                for sub in subdomains:
                                    print(Fore.WHITE + f" - {sub}.{domain}")
                                    with open('result_file.txt', 'a') as result_file:
                                        result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - {sub}.{domain}\n")
                                        result_file.flush()
                            else:
                                print(Fore.YELLOW + " - No subdomains found.")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - No subdomains found.\n")
                                    result_file.flush()
                        except Exception as e:
                            logging.error(f"Component Subdomains: Error fetching subdomains: {e}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component Subdomains: Error fetching subdomains: {e}\n")
                                result_file.flush()
                            print(Fore.RED + f"Error fetching subdomains: {e}")


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
                            domain_info = whois.whois(domain)
                            admin_email = domain_info.get('emails')
                            if admin_email:
                                print(Fore.WHITE + f" - Admin Email: {admin_email}")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Admin Email: {admin_email}\n")
                                    result_file.flush()
                            else:
                                print(Fore.YELLOW + " - Admin email not found.")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Admin email not found.\n")
                                    result_file.flush()
                        except Exception as e:
                            logging.error(f"Error fetching admin email: {e}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Error fetching admin email: {e}\n")
                                result_file.flush()
                            print(self.errors_color + f"Error fetching admin email: {e}")
                        
                        try:
                            domain_info = whois.whois(domain)
                            registrant_org = domain_info.get('org')
                            if registrant_org:
                                print(Fore.WHITE + f" - Registrant Organization: {registrant_org}")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Registrant Organization: {registrant_org}\n")
                                    result_file.flush()
                            else:
                                print(Fore.YELLOW + " - Registrant Organization not found.")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Registrant Organization not found.\n")
                                    result_file.flush()
                        except Exception as e:
                            logging.error(f"Error fetching registrant organization: {e}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Error fetching registrant organization: {e}\n")
                                result_file.flush()
                            print(self.errors_color + f"Error fetching registrant organization: {e}")
                        
                        try:
                            domain_info = whois.whois(domain)
                            registrant_name = domain_info.get('name')
                            if registrant_name:
                                print(Fore.WHITE + f" - Registrant Name: {registrant_name}")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Registrant Name: {registrant_name}\n")
                                    result_file.flush()
                            else:
                                print(Fore.YELLOW + " - Registrant Name not found.")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Registrant Name not found.\n")
                                    result_file.flush()
                        except Exception as e:
                            logging.error(f"Error fetching registrant name: {e}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Error fetching registrant name: {e}\n")
                                result_file.flush()
                            print(self.errors_color + f"Error fetching registrant name: {e}")
                        
                        try:
                            domain_info = whois.whois(domain)
                            copyright = domain_info.get('copyright')
                            if copyright:
                                print(Fore.WHITE + f" - Copyright: {copyright}")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Copyright: {copyright}\n")
                                    result_file.flush()
                            else:
                                print(Fore.YELLOW + " - Copyright information not found.")
                                with open('result_file.txt', 'a') as result_file:
                                    result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Copyright information not found.\n")
                                    result_file.flush()
                        except Exception as e:
                            logging.error(f"Error fetching copyright information: {e}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Error fetching copyright information: {e}\n")
                                result_file.flush()
                            print(self.errors_color + f"Error fetching copyright information: {e}")
                            
                        try:
                            domain_info = whois.whois(domain)
                            creation_date = domain_info.get('creation_date')
                            if creation_date:
                                age = datetime.now() - creation_date
                                print(Fore.WHITE + f" - Domain Age: {age.days} days")
                            else:
                                print(Fore.YELLOW + " - Domain creation date not found.")
                        except Exception as e:
                            print(self.errors_color + f"Domain age error: {e}")
                            logging.error(f"Domain age error: {e}")
                        
                        try:
                            tld = domain.split('.')[-1]
                            print(Fore.WHITE + f" - Domain Type: {tld}")
                            with open('result_file.txt', 'a') as result_file:
                                result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Domain Type: {tld}\n")
                                result_file.flush()
                        except Exception as e:
                            logging.error(f"Component WHOIS: Domain Type error: {e}")
                            result_file.write(f"{datetime.now().strftime('%d_%m_%Y_%H_%M')} - Component WHOIS: Domain Type error: {e}\n")
                            result_file.flush()
                            print(self.errors_color + f"Domain Type error: {e}")
                            
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

        class projects:
            def create_new_project(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color+self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(" ")
                print(Fore.WHITE+" Welcome to SXSCLI:PROJECTS!")
                logging.info("Component PROJECTS: Successfully launched.")
                
                print(Fore.WHITE+"""
 Projects are a very interesting part of SXServiseCLI! 
 Here you can create your own project, register your application and 
 get a mini key to optimize the application. Note that certain restrictions apply to each key.

 - Create a project - 1
 - Back - 0 or exit
""")
                x = input(Fore.WHITE + " & >>> ")
                if x == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color+self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    print("Project information:")
                    project_name = input(Fore.WHITE + " - Enter project name: ")
                    project_description = input(Fore.WHITE + " - Enter project description: ")
                    print("Your information:")
                    full_name = input(Fore.WHITE + " - Enter your Full Name: ")
                    phone_number = input(Fore.WHITE + " - Enter your Phone Number: ")
                    email = input(Fore.WHITE + " - Enter your Email: ")
                    date_of_birth = input(Fore.WHITE + " - Enter your Date of Birth (DD-MM-YYYY): ")
                    print("BETA FUNC")
                    SXServiseCLI.System.run_input(self)
                    
                    
                    
                elif x == "0" or x.lower() == "exit":
                    SXServiseCLI.System.run_input(self)
                
        def Search(self, promt):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color+self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            logging.info("Component SEARCH: Successfully launched.")
            print(" ")
            print(Fore.WHITE+"Searching in progress...")
            logging.info(f" Component SEARCH: Searching for: {promt}")
            print(self.search_engine.search(promt))
            print(Fore.WHITE+" ")
            SXServiseCLI.System.run_input(self)
        
        def upgrade(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color+self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(Fore.WHITE+" Welcome to SXSCLI:UPGRADE!")
            logging.info("Component UPGRADE: Successfully launched.")
            print(Fore.WHITE+f"""
 To get the former functionality, you can go to our official website and 
 buy + or pro version. All your purchases help our team develop the project. 
 Our goal is to create a project that can improve and help you improve your knowledge 
 without advertising, even in the free version.

 Official Website: https://www.sxservisecli.tech/
""")
            SXServiseCLI.System.run_input(self)
        
        def status(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color+self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(Fore.WHITE+" Welcome to SXSCLI:STATYS!")
            logging.info("Component STATYS: Successfully launched.")
            print(Fore.WHITE+f"""
 All systems are functioning properly, and all core components are performing at optimal levels. 
 Our system status is continuously monitored to ensure smooth operation. We strive to keep everything 
 up-to-date and running without interruptions, providing a seamless experience for our users.

 Status Page: https://sx.statuspage.io/
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
   init - Initialize the applicationd  
   support - Official technical support
   pers - Personalization settings
   config - Configuration settings
   upgrade - Buy a better version
   about - Software information
 - - - - - - - - - - - - - - - - CYBER SECURITY - - - - - - - - - - - - - - - -      < - - - Dangerous* commands
   whois - Domain check
   pscan - Port scan
   faker - Generate fake information (For registration, etc.)
   netmon - Network monitoring
   networkinfo - Obtaining detailed information about the network
 - - - - - - - - - - - - - - - - - - TOOLS - - - - - - - - - - - - - - - - - - -     < - - - Internal tools 
   ftp - File Transfer Protocol client (FTP)
   ssh - Secure Shell protocol client (SSH)
   db - Database management system (DB)
   ping - Ping server (PING)
   device - Device information 
   qrcode - QR code generator (QRCode)
 - - - - - - - - - - - - - - Artificial intelligence - - - - - - - - - - - - - -     < - - - Additional* commands
   genai - Chat with AI (Google AI Studio)
   ai - Interface for launching artificial intelligence
   mediapipe - Try AI using your camera
   playground - Playground for developers (SOON)
   create - Create a new AI (SOON)
 - - - - - - - - - - - - - - - - - - PLATFORMS - - - - - - - - - - - - - - - - - -   < - - - Additional* commands
   build - Manage your projects (SOON)
   learn - Learn programming languages (SOON)
   try   - Try new technologies (SOON)
 - - - - - - - - - - - - - - - - - - - Other - - - - - - - - - - - - - - - - - - -   < - - - Global* commands
   ip - Get your IP address
   mac - Get your MAC address
   cpu - Get information about the CPU
   gpu - Get information about the GPU
   clear - Clear the console
   speedtest - Check the speed of the Internet connection
   exit - Exit the application
   . - Clear logs
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   < - - - What is this?
  SXServiseCLI 2024 - is a powerful and versatile command-line tool 
  that helps you run local services, generate JSON files, create QR codes, 
  test APIs, SSH, FTP, and much more.

  Copyright (c) 2023-2025 Kozosvyst Stas (StasX) 
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
                print(Fore.WHITE +
f"""
 User Information:
    Nickname       : {self.user_cfg["nickname"]}
    Full Name      : {self.user_cfg["fullname"]}
    Email          : {self.user_cfg["mail"]}
    IP Address     : {user_ip} 
    Mode           : {self.user_cfg["MODE"]}

 CLI Information:
    CLI Name       : {self.app_name}
    CLI Version    : {self.app_version}
    CLI ID         : {self.app_id}
    CLI Command    : {self.app_com}
    CLI API        : {str(self.settings_api)}
    CLI AuthAPI    : {str(self.settings_AuthAPI)}

 Useful Links:
    GitHub         : https://github.com/StasX-Official/SXServiseCLI
    Official Site  : https://sxcomp.42web.io/p/SXServiseCLI
    Official Wiki  : https://github.com/StasX-Official/SXServiseCLI/wiki
""")
            SXServiseCLI.System.run_input(self)
        
        class qrcode:
            def run(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color + self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(" ")
                print(Fore.WHITE + " Welcome to SXSCLI:QRCode!")
                logging.info("Component QRCODE: Successfully launched.")
                print(Fore.WHITE + """
 QR codes are two-dimensional barcodes that store data, which can be scanned 
 by smartphones or QR readers. They are commonly used for quick access to websites, 
 payment systems, or information.
 
 [0] Exit QRCode                              [5] Generate a colored QR code                       [10] Generate a QR code for geolocation
 [1] Generate a basic QR code                 [6] Generate a WiFi QR code                          [11] Generate a QR code for calendar event
 [2] Generate a QR code with a custom size    [7] Generate a payment QR code (e.g., PayPal)
 [3] Generate a QR code with a logo           [8] Generate a QR code for a website
 [4] Generate an SVG QR code                  [9] Generate a QR code for contact details (vCard)

        """)
                choice = input(Fore.WHITE+ " >>> ")

                if choice == "0":
                    SXServiseCLI.System.run_input(self)
                elif choice == "1":
                    SXServiseCLI.System.qrcode.generate_basic_qr(self)
                elif choice == "2":
                    SXServiseCLI.System.qrcode.generate_custom_size_qr(self)
                elif choice == "3":
                    SXServiseCLI.System.qrcode.generate_logo_qr(self)
                elif choice == "4":
                    SXServiseCLI.System.qrcode.generate_svg_qr(self)
                elif choice == "5":
                    SXServiseCLI.System.qrcode.generate_colored_qr(self)
                elif choice == "6":
                    SXServiseCLI.System.qrcode.generate_wifi_qr(self)
                elif choice == "7":
                    SXServiseCLI.System.qrcode.generate_payment_qr(self)
                elif choice == "8":
                    SXServiseCLI.System.qrcode.generate_website_qr(self)
                elif choice == "9":
                    SXServiseCLI.System.qrcode.generate_vcard_qr(self)
                elif choice == "10":
                    SXServiseCLI.System.qrcode.generate_geolocation_qr(self)
                elif choice == "11":
                    SXServiseCLI.System.qrcode.generate_event_qr(self)
                else:
                    print(Fore.RED + "Invalid choice. Please try again.")
                    SXServiseCLI.System.run_input(self)

            def generate_basic_qr(self):
                try:
                    data = Prompt.ask("Enter the data for the QR code")
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr = qrcode.make(data)
                    qr_path = os.path.join(output_dir, "basic_qr.png")
                    qr.save(qr_path)
                    self.console.print(f"[green]Basic QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: Basic QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating basic QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating basic QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_custom_size_qr(self):
                try:
                    data = Prompt.ask("Enter the data for the QR code")
                    size = int(Prompt.ask("Enter the size for the QR code (e.g., 10)", default="10"))
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr = qrcode.QRCode(version=size, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
                    qr.add_data(data)
                    qr.make(fit=True)
                    qr_path = os.path.join(output_dir, "custom_size_qr.png")
                    img = qr.make_image(fill_color="black", back_color="white")
                    img.save(qr_path)
                    self.console.print(f"[green]Custom size QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: Custom size QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating custom size QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating custom size QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_logo_qr(self):
                try:
                    data = Prompt.ask("Enter the data for the QR code")
                    logo_path = Prompt.ask("Enter the path to the logo image")
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
                    qr.add_data(data)
                    qr.make(fit=True)
                    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
                    logo = Image.open(logo_path)
                    box = (img.size[0] // 4, img.size[1] // 4, img.size[0] * 3 // 4, img.size[1] * 3 // 4)
                    logo = logo.resize((box[2] - box[0], box[3] - box[1]))
                    img.paste(logo, box)
                    qr_path = os.path.join(output_dir, "logo_qr.png")
                    img.save(qr_path)
                    self.console.print(f"[green]QR code with logo saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: QR code with logo saved.")
                except FileNotFoundError:
                    self.console.print(f"[red]Logo file not found: {logo_path}[/red]")
                    logging.error(f"Component QRCODE: Logo file not found: {logo_path}")
                except Exception as e:
                    self.console.print(f"[red]Error generating QR code with logo: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating QR code with logo: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_svg_qr(self):
                try:
                    data = Prompt.ask("Enter the data for the QR code")
                    factory = qrcode.image.svg.SvgImage
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    img = qrcode.make(data, image_factory=factory)
                    qr_path = os.path.join(output_dir, "svg_qr.svg")
                    img.save(qr_path)
                    self.console.print(f"[green]SVG QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: SVG QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating SVG QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating SVG QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_colored_qr(self):
                try:
                    data = Prompt.ask("Enter the data for the QR code")
                    fill_color = Prompt.ask("Enter the fill color (e.g., 'red')")
                    back_color = Prompt.ask("Enter the background color (e.g., 'yellow')")
                    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
                    qr.add_data(data)
                    qr.make(fit=True)
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr_path = os.path.join(output_dir, "colored_qr.png")
                    img = qr.make_image(fill_color=fill_color, back_color=back_color)
                    img.save(qr_path)
                    self.console.print(f"[green]Colored QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: Colored QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating colored QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating colored QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_wifi_qr(self):
                try:
                    ssid = Prompt.ask("Enter the WiFi SSID")
                    password = Prompt.ask("Enter the WiFi password", password=True)
                    authentication = Prompt.ask("Enter the authentication type (WPA/WEP)", choices=["WPA", "WEP"], default="WPA")
                    wifi_data = f"WIFI:S:{ssid};T:{authentication};P:{password};;"
                    qr = qrcode.make(wifi_data)
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr_path = os.path.join(output_dir, "wifi_qr.png")
                    qr.save(qr_path)
                    self.console.print(f"[green]WiFi QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: WiFi QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating WiFi QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating WiFi QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_payment_qr(self):
                try:
                    platform = Prompt.ask("Enter the payment platform (e.g., PayPal)")
                    account = Prompt.ask("Enter the account details")
                    amount = Prompt.ask("Enter the amount to be paid")
                    payment_data = f"PAYMENT:{platform};ACCOUNT:{account};AMOUNT:{amount};;"
                    qr = qrcode.make(payment_data)
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr_path = os.path.join(output_dir, "payment_qr.png")
                    qr.save(qr_path)
                    self.console.print(f"[green]Payment QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: Payment QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating payment QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating payment QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_website_qr(self):
                try:
                    url = Prompt.ask("Enter the URL for the QR code")
                    qr = qrcode.make(url)
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr_path = os.path.join(output_dir, "website_qr.png")
                    qr.save(qr_path)
                    self.console.print(f"[green]Website QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: Website QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating website QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating website QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_vcard_qr(self):
                try:
                    name = Prompt.ask("Enter the full name")
                    phone = Prompt.ask("Enter the phone number")
                    email = Prompt.ask("Enter the email address")
                    vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"
                    qr = qrcode.make(vcard_data)
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr_path = os.path.join(output_dir, "vcard_qr.png")
                    qr.save(qr_path)
                    self.console.print(f"[green]Contact details QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: Contact details QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating contact details QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating contact details QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_geolocation_qr(self):
                try:
                    latitude = Prompt.ask("Enter the latitude")
                    longitude = Prompt.ask("Enter the longitude")
                    geo_data = f"geo:{latitude},{longitude}"
                    qr = qrcode.make(geo_data)
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr_path = os.path.join(output_dir, "geo_qr.png")
                    qr.save(qr_path)
                    self.console.print(f"[green]Geolocation QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: Geolocation QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating geolocation QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating geolocation QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def generate_event_qr(self):
                try:
                    summary = Prompt.ask("Enter the event summary")
                    location = Prompt.ask("Enter the event location")
                    start_time = Prompt.ask("Enter the start time (YYYYMMDDTHHMMSS)")
                    end_time = Prompt.ask("Enter the end time (YYYYMMDDTHHMMSS)")
                    event_data = f"BEGIN:VEVENT\nSUMMARY:{summary}\nLOCATION:{location}\nDTSTART:{start_time}\nDTEND:{end_time}\nEND:VEVENT"
                    qr = qrcode.make(event_data)
                    output_dir = "Staff/results"
                    os.makedirs(output_dir, exist_ok=True)
                    qr_path = os.path.join(output_dir, "event_qr.png")
                    qr.save(qr_path)
                    self.console.print(f"[green]Event QR code saved as '{qr_path}'[/green]")
                    logging.info("Component QRCODE: Event QR code saved.")
                except Exception as e:
                    self.console.print(f"[red]Error generating event QR code: {e}[/red]")
                    logging.error(f"Component QRCODE: Error generating event QR code: {e}")
                finally:
                    SXServiseCLI.System.run_input(self) 
    
        class db:
            def run(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color + self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(" ")
                print(Fore.WHITE + " Welcome to SXSCLI:DB!")
                logging.info("Component DB: Successfully launched.")
                print("""
    Please choose an option: (BETA)
        
        [0] Exit Database Manager
        [1] Open existing database (.db file)  (SOON)
        [2] Create a new SQLite database (.db file)
        [3] Connect to an existing SQLite database
        [4] Connect to MySQL database
        """)
                cmd_input = input(Fore.WHITE + " - Enter a command: ").strip().lower()
                if int(cmd_input) == 0:
                    SXServiseCLI.System.run_input(self)
                elif int(cmd_input) == 1:
                    print(Fore.RED + " - This feature is coming soon.")
                    SXServiseCLI.System.run_input(self)
                elif int(cmd_input) == 2:
                    SXServiseCLI.System.db.create_sqlite_db(self)
                elif int(cmd_input) == 3:
                    SXServiseCLI.System.db.connect_sqlite_db(self)
                elif int(cmd_input) == 4:
                    SXServiseCLI.System.db.connect_mysql_db(self)
                else:
                    print(Fore.RED + " - Incorrect command.")
                    logging.error("Component DB: Incorrect command.")
                    SXServiseCLI.System.run_input(self)

            def create_sqlite_db(self):
                db_name = input(Fore.WHITE + " - Enter new SQLite database name: ").strip()
                try:
                    self.connection = sqlite3.connect(f"{db_name}.db")
                    self.cursor = self.connection.cursor()
                    print(Fore.GREEN + " - SQLite database created successfully!")
                    logging.info(f"Component DB: SQLite database '{db_name}' created successfully.")
                    SXServiseCLI.System.db.create_tables(self)
                    self.connection.commit()

                except sqlite3.Error as e:
                    print(Fore.RED + f" - Failed to create database: {e}")
                    logging.error(f"Component DB: Failed to create SQLite database '{db_name}'. Error: {e}")
                finally:
                    if self.connection:
                        self.connection.close()
                        print(Fore.YELLOW + " - Connection closed.")

            def create_tables(self):
                print(Fore.WHITE + " - Creating tables in the new database...")
                table_name = input(Fore.WHITE + " - Enter table name: ").strip()
                columns_input = input(Fore.WHITE + " - Enter column names and types (e.g., 'id INTEGER PRIMARY KEY, name TEXT'): ").strip()

                create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_input});"
                try:
                    self.cursor.execute(create_table_query)
                    print(Fore.GREEN + f" - Table '{table_name}' created successfully!")
                    logging.info(f"Component DB: Table '{table_name}' created successfully in the new SQLite database.")
                except sqlite3.Error as e:
                    print(Fore.RED + f" - Failed to create table: {e}")
                    logging.error(f"Component DB: Failed to create table '{table_name}'. Error: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

            def connect_sqlite_db(self):
                db_name = input(Fore.WHITE + " - Enter the SQLite database name to connect: ").strip()
                try:
                    self.connection = sqlite3.connect(f"{db_name}.db")
                    self.cursor = self.connection.cursor()
                    print(Fore.GREEN + " - Connected to SQLite database successfully!")
                    logging.info(f"Component DB: Connected to SQLite database '{db_name}' successfully.")
                    SXServiseCLI.System.db.run_sql_commands(self)
                except sqlite3.Error as e:
                    print(Fore.RED + f" - Failed to connect to database: {e}")
                    logging.error(f"Component DB: Failed to connect to SQLite database '{db_name}'. Error: {e}")
                finally:
                    if self.connection:
                        self.connection.close()
                        print(Fore.YELLOW + " - Connection closed.")
                        SXServiseCLI.System.run_input(self)
                    SXServiseCLI.System.run_input(self)

            def run_sql_commands(self):
                while True:
                    print(Fore.WHITE + "\n - Enter an SQL command (type 'exit' to stop):")
                    sql_command = input(Fore.WHITE + " SQL> ").strip()

                    if sql_command.lower() == 'exit':
                        print(Fore.YELLOW + " - Exiting SQL command interface...")
                        break

                    try:
                        self.cursor.execute(sql_command)
                        if sql_command.strip().lower().startswith('select'):
                            rows = self.cursor.fetchall()
                            for row in rows:
                                print(row)
                        else:
                            self.connection.commit()
                            print(Fore.GREEN + " - Command executed successfully!")
                    except sqlite3.Error as e:
                        print(Fore.RED + f" - Error executing command: {e}")
                        logging.error(f"Component DB: Error executing command: {e}")
                SXServiseCLI.System.run_input(self)

            def connect_mysql_db(self):
                host = input(Fore.WHITE + " - Enter MySQL host: ").strip()
                user = input(Fore.WHITE + " - Enter MySQL username: ").strip()
                password = input(Fore.WHITE + " - Enter MySQL password: ").strip()
                database = input(Fore.WHITE + " - Enter MySQL database name: ").strip()

                try:
                    self.connection = mysql.connector.connect(
                        host=host,
                        user=user,
                        password=password,
                        database=database
                    )
                    self.cursor = self.connection.cursor()
                    if self.connection.is_connected():
                        print(Fore.GREEN + " - Connected to MySQL database successfully!")
                        logging.info(f"Component DB: Connected to MySQL database '{database}' on host '{host}' successfully.")

                        SXServiseCLI.System.db.run_mysql_commands()

                except mysql.connector.Error as e:
                    print(Fore.RED + f" - Failed to connect to MySQL database: {e}")
                    logging.error(f"Component DB: Failed to connect to MySQL database '{database}' on host '{host}'. Error: {e}")
                finally:
                    if self.connection and self.connection.is_connected():
                        self.connection.close()
                        print(Fore.YELLOW + " - Connection closed.")
                        SXServiseCLI.System.run_input(self)
                    

            def run_mysql_commands(self):
                while True:
                    print(Fore.WHITE + "\n - Enter an SQL command (type 'exit' to stop):")
                    sql_command = input(Fore.WHITE + " SQL> ").strip()

                    if sql_command.lower() == 'exit':
                        print(Fore.YELLOW + " - Exiting SQL command interface...")
                        break

                    try:
                        self.cursor.execute(sql_command)
                        if sql_command.strip().lower().startswith('select'):
                            rows = self.cursor.fetchall()
                            for row in rows:
                                print(row)
                        else:
                            self.connection.commit()
                            print(Fore.GREEN + " - Command executed successfully!")
                    except mysql.connector.Error as e:
                        print(Fore.RED + f" - Error executing command: {e}")
                        logging.error(f"Component DB: Error executing command: {e}")
                    finally:
                        SXServiseCLI.System.run_input(self)
        
        class netmon:
            def netmon(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color+self.logo)
                print(" ")
                console=self.console
                console.print("[bold green]Monitoring network activity. Press Ctrl+C to stop.[/bold green]")
                try:
                    while True:
                        net_io = psutil.net_io_counters()
                        console.print(f"\n[bold yellow]Total Bytes Sent:[/bold yellow] {net_io.bytes_sent / (1024 * 1024):.2f} MB")
                        console.print(f"[bold yellow]Total Bytes Received:[/bold yellow] {net_io.bytes_recv / (1024 * 1024):.2f} MB")
                        console.print(f"[bold yellow]Total Packets Sent:[/bold yellow] {net_io.packets_sent}")
                        console.print(f"[bold yellow]Total Packets Received:[/bold yellow] {net_io.packets_recv}")

                        console.print("\n[bold cyan]Network Adapters Status:[/bold cyan]")
                        for adapter, stats in psutil.net_if_addrs().items():
                            table = Table(show_header=True, header_style="bold magenta")
                            table.add_column("Adapter", style="bold")
                            table.add_column("Type", style="bold")
                            table.add_column("Address", style="bold")
                            for snic in stats:
                                if snic.family == socket.AF_INET:
                                    table.add_row(adapter, "IPv4", snic.address)
                                elif snic.family == socket.AF_INET6:
                                    table.add_row(adapter, "IPv6", snic.address)
                                elif snic.family == psutil.AF_LINK:
                                    table.add_row(adapter, "MAC", snic.address)
                            console.print(table)


                        console.print("\n[bold cyan]Active Network Connections:[/bold cyan]")
                        table = Table(show_header=True, header_style="bold green")
                        table.add_column("Local Address", style="bold")
                        table.add_column("Remote Address", style="bold")
                        table.add_column("Status", style="bold")
                        for conn in psutil.net_connections(kind='inet'):
                            laddr = conn.laddr
                            raddr = conn.raddr
                            status = conn.status
                            table.add_row(f"{laddr.ip}:{laddr.port}", f"{raddr.ip if raddr else 'None'}:{raddr.port if raddr else 'None'}", status)
                        console.print(table)

                        console.print("\n[bold cyan]Network Process Activity:[/bold cyan]")
                        table = Table(show_header=True, header_style="bold red")
                        table.add_column("PID", style="bold")
                        table.add_column("Process Name", style="bold")
                        table.add_column("Local Address", style="bold")
                        table.add_column("Remote Address", style="bold")
                        for proc in psutil.process_iter(['pid', 'name']):
                            try:
                                connections = proc.connections(kind='inet')
                                for conn in connections:
                                    if conn.status == 'ESTABLISHED':
                                        laddr = conn.laddr
                                        raddr = conn.raddr
                                        table.add_row(str(proc.info['pid']), proc.info['name'], f"{laddr.ip}:{laddr.port}", f"{raddr.ip if raddr else 'None'}:{raddr.port if raddr else 'None'}")
                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                                pass
                        console.print(table)

                        console.print("-" * 50)
                        time.sleep(1)

                except KeyboardInterrupt:
                    console.print("\n[bold red]Network monitoring stopped.[/bold red]")
                    SXServiseCLI.System.run_input(self)
            
            def run(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color+self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(Fore.WHITE+" Welcome to SXSCLI:NETMON!")
                logging.info("Component NETMON: Successfully launched.")
                print("""
 - Welcome to the Network Monitor!
 
 This is a dangerous feature. If you continue, you will:
  1. You take full responsibility for your actions.
  2. You agree to all of our rules and policies. (Info on our website) """)
                action = input(Fore.WHITE+" - Continue? (y/n): ").strip().lower()
                if action == "y":
                    print(Fore.WHITE+" ")
                    SXServiseCLI.System.netmon.netmon(self)
                else:
                    SXServiseCLI.System.run_input(self)
        
        class ping:
            def ping(self,host):
                param = "-n" if platform.system().lower() == "windows" else "-c"
                command = ["ping", param, "4", host]
                console=self.console
                console.print(Panel("[bold cyan]PING[/bold cyan]"))
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
        
        class faker:
            def run(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color + self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(" ")
                logging.info("Component FAKER: Successfully launched.")
                print(Fore.WHITE + """
 - Welcome to the Fake Identity Generator(PRE)!
 - What will we generate today?
 
 - Exit           - exit
 - Fake email     - fakemail
 - Fake credit card info - fakecard
 - Fake address          - fakeaddress
 - Fake human info       - fakehuman
 - Fake phone number     - fakephone
 - Fake job title        - fakejob
 - Fake company name     - fakecompany
 - Fake date of birth    - fakedob
 - Fake username         - fakeusername
 - Bulk generate         - bulk
                """)
                
                action = input(Fore.WHITE + " >>> ").strip().lower()
                try:
                    if action == "exit":
                        print(Fore.WHITE + "Exiting...")
                    elif action == "fakecard":
                        print(Fore.WHITE + f"Fake credit card info: ")
                        print(f"Card Number: {random.randint(1000000000000000, 9999999999999999)}\nExpiry: {random.randint(1, 12)}/{random.randint(23, 30)}\nCVV: {random.randint(100, 999)}")
                    elif action == "fakehuman":
                        print(Fore.WHITE + f"Fake human info: ")
                        first_name = random.choice(["John", "Jane", "Sam", "Sara", "Mike", "Anna"])
                        last_name = random.choice(["Doe", "Smith", "Johnson", "Williams", "Jones"])
                        age = random.randint(18, 80)
                        print(f"Name: {first_name} {last_name}\nAge: {age}")
                    elif action == "fakemail":
                        print(Fore.WHITE + f"Fake email: ")
                        print(f"email{random.randint(1000, 9999)}@fake.com")
                    elif action == "fakeaddress":
                        print(Fore.WHITE + f"Fake address: ")
                        street = random.choice(["123 Main St", "456 Elm St", "789 Oak St"])
                        city = random.choice(["Springfield", "Riverside", "Franklin"])
                        zip_code = random.randint(10000, 99999)
                        print(f"Address: {street}, {city}, {zip_code}")
                    elif action == "fakephone":
                        print(Fore.WHITE + f"Fake phone number: ")
                        print(f"+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}")
                    elif action == "fakejob":
                        print(Fore.WHITE + f"Fake Job Title: ")
                        print(random.choice(["Software Developer", "Project Manager", "Data Scientist", "Graphic Designer", "Marketing Specialist"]))
                    elif action == "fakecompany":
                        print(Fore.WHITE + f"Fake Company Name: ")
                        print(random.choice(["TechCorp", "Innovate Solutions", "Global Enterprises", "FutureWorks", "Creative Labs"]))
                    elif action == "fakedob":
                        print(Fore.WHITE + f"Fake Date of Birth: ")
                        year = random.randint(1960, 2005)
                        month = random.randint(1, 12)
                        day = random.randint(1, 28)
                        print(f"Date of Birth: {month}/{day}/{year}")
                    elif action == "fakeusername":
                        print(Fore.WHITE + f"Fake Username: ")
                        print(''.join(random.choices(string.ascii_letters + string.digits, k=8)))
                    elif action == "bulk":
                        try:
                            count = int(input(Fore.WHITE + "How many entries to generate? "))
                            if count <= 0:
                                print(Fore.RED + " -> Invalid count. Please enter a positive integer.")
                            else:
                                data_type = input(Fore.WHITE + "What type of data to generate? ").strip().lower()

                                if data_type == "fakecard":
                                    generator_function = lambda: f"Card Number: {random.randint(1000000000000000, 9999999999999999)}\nExpiry: {random.randint(1, 12)}/{random.randint(23, 30)}\nCVV: {random.randint(100, 999)}"
                                elif data_type == "fakehuman":
                                    generator_function = lambda: f"Name: {random.choice(['John', 'Jane', 'Sam', 'Sara', 'Mike', 'Anna'])} {random.choice(['Doe', 'Smith', 'Johnson', 'Williams', 'Jones'])}\nAge: {random.randint(18, 80)}"
                                else:
                                    print(Fore.RED + " -> Invalid data type.")
                                    return
                                
                                print(Fore.WHITE + f"Generating {count} entries of {data_type}:")
                                for i in range(count):
                                    print(Fore.WHITE + f"--- Entry {i + 1} ---")
                                    print(generator_function())
                                    
                        except ValueError:
                            logging.error("Component FAKER: Invalid input. Please enter a valid integer for count.")
                            print(Fore.RED + " -> Invalid input. Please enter a valid integer for count.")
                            SXServiseCLI.System.run_input(self)
                    else:
                        logging.error("Component FAKER: Invalid action.")
                        print(Fore.RED + " -> Sorry, Invalid action.")
                        SXServiseCLI.System.run_input(self)
                except Exception as e:
                    logging.error(f"Component FAKER: An unexpected error occurred: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)
        
        def ai(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.logo_color+self.logo)
            print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
            print(Fore.WHITE+" Welcome to SXSCLI:AI!")
            print(" ")
            logging.info("Component AI: Successfully launched.")
            print("Turn off: Ctrl+C")
            while True:
                try:
                    from System.sxscli_web_core import AI_WITH_WEB_INTERFACE
                    ai_interface = AI_WITH_WEB_INTERFACE()
                    ai_interface.start()
                except KeyboardInterrupt:
                    SXServiseCLI.System.run_input(self)
                except Exception as e:
                    print(Fore.RED + " -> Sorry, AI interface failed to start.")
                    logging.error(f"Component AI: AI interface failed to start. ERROR: {e}")
                    SXServiseCLI.System.run_input(self)
                finally:
                    SXServiseCLI.System.run_input(self)
        
        class networkinfo:
            def run(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color+self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(Fore.WHITE+" Welcome to SXSCLI:NETINFO!")
                print(Fore.WHITE+" ")
                logging.info("Component NETINFO: Successfully launched.")
                try:
                    hostname = socket.gethostname()
                    local_ip = socket.gethostbyname(hostname)
                    interfaces = psutil.net_if_addrs()
                    net_stats = psutil.net_if_stats()
                    system_info = platform.system()
                    system_version = platform.version()
                    print(f"System Info: {system_info} {system_version}")
                    print(f"Hostname: {hostname}")
                    print(f"Local IP: {local_ip}")
                    print("\nNetwork Interfaces:")
                    if not interfaces:
                        print("  No network interfaces found.")
                    for interface, addrs in interfaces.items():
                        print(f"\nInterface: {interface}")
                        for addr in addrs:
                            print(f"  - Address: {addr.address}")
                            print(f"  - Netmask: {addr.netmask}")
                            print(f"  - Broadcast: {addr.broadcast}")
                        if interface in net_stats:
                            stats = net_stats[interface]
                            print(f"  - Is Up: {stats.isup}")
                            print(f"  - Duplex: {stats.duplex}")
                            print(f"  - Speed: {stats.speed} Mbps")
                        else:
                            print(f"  - No stats available for {interface}")
                except socket.gaierror as e:
                    print(f"Error: Unable to retrieve hostname or IP address. Details: {e}")
                except psutil.NoSuchProcess as e:
                    print(f"Error: Problem with network interfaces or process. Details: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)

        class api:
            def action_process(self, action):
                try:
                    if action == "0":
                        print(Fore.WHITE + "Exiting API Tester...")
                        SXServiseCLI.System.run_input(self)
                    elif action == "1":
                        print(Fore.WHITE + "Pinging API (example.com)...")
                        try:
                            response = requests.get("https://example.com")
                            if response.status_code == 200:
                                print(Fore.GREEN + "API is reachable.")
                            else:
                                print(Fore.RED + f"API is unreachable. Status code: {response.status_code}")
                        except requests.exceptions.RequestException as e:
                            print(Fore.RED + f"Error: {e}")
                    elif action == "2":
                        api_url = input(Fore.WHITE + "Enter API URL to check status: ")
                        try:
                            response = requests.get(api_url)
                            print(Fore.WHITE + f"API Status Code: {response.status_code}")
                        except requests.exceptions.RequestException as e:
                            print(Fore.RED + f"Error: {e}")

                    elif action == "3":
                        api_url = input(Fore.WHITE + "Enter GET API URL: ")
                        try:
                            response = requests.get(api_url)
                            response.raise_for_status()
                            print(Fore.WHITE + "Response:")
                            try:
                                print(json.dumps(response.json(), indent=4))
                            except json.JSONDecodeError:
                                print(response.text)
                        except requests.exceptions.RequestException as e:
                            print(Fore.RED + f"Error: {e}")

                    elif action == "4":
                        api_url = input(Fore.WHITE + "Enter POST API URL: ")
                        data = input(Fore.WHITE + "Enter POST data (JSON format): ")
                        try:
                            data = json.loads(data)
                            response = requests.post(api_url, json=data)
                            response.raise_for_status()
                            print(Fore.WHITE + "Response:")
                            print(json.dumps(response.json(), indent=4))
                        except (json.JSONDecodeError, requests.exceptions.RequestException) as e:
                            print(Fore.RED + f"Error: {e}")

                    elif action == "5":
                        api_url = input(Fore.WHITE + "Enter API URL: ")
                        auth_type = input(Fore.WHITE + "Enter authentication type (basic/bearer): ").lower()

                        if auth_type == "basic":
                            username = input(Fore.WHITE + "Enter username: ")
                            password = input(Fore.WHITE + "Enter password: ")
                            try:
                                response = requests.get(api_url, auth=(username, password))
                                response.raise_for_status()
                                print(Fore.GREEN + "Authentication successful.")
                            except requests.exceptions.RequestException as e:
                                print(Fore.RED + f"Authentication failed: {e}")
                        elif auth_type == "bearer":
                            token = input(Fore.WHITE + "Enter bearer token: ")
                            headers = {'Authorization': f'Bearer {token}'}
                            try:
                                response = requests.get(api_url, headers=headers)
                                response.raise_for_status()
                                print(Fore.GREEN + "Authentication successful.")
                            except requests.exceptions.RequestException as e:
                                print(Fore.RED + f"Authentication failed: {e}")
                        else:
                            print(Fore.RED + "Invalid authentication type.")

                    elif action == "6":
                        api_url = input(Fore.WHITE + "Enter PUT API URL: ")
                        data = input(Fore.WHITE + "Enter PUT data (JSON format): ")
                        try:
                            data = json.loads(data)
                            response = requests.put(api_url, json=data)
                            response.raise_for_status()
                            print(Fore.WHITE + "Response:")
                            print(json.dumps(response.json(), indent=4))
                        except (json.JSONDecodeError, requests.exceptions.RequestException) as e:
                            print(Fore.RED + f"Error: {e}")

                    elif action == "7" or action == "8":
                        api_url = input(Fore.WHITE + "Enter DELETE API URL: ")
                        try:
                            response = requests.delete(api_url)
                            response.raise_for_status()
                            print(Fore.GREEN + "DELETE request successful.")
                            if response.text:
                                print(Fore.WHITE + "Response:")
                                print(response.text)
                        except requests.exceptions.RequestException as e:
                            print(Fore.RED + f"Error: {e}")

                    elif action == "9":
                        api_url = input(Fore.WHITE + "Enter XML API URL: ")
                        try:
                            response = requests.get(api_url)
                            response.raise_for_status()
                            root = ET.fromstring(response.content)
                            print(Fore.WHITE + "XML Response:")
                            ET.dump(root)
                        except requests.exceptions.RequestException as e:
                            print(Fore.RED + f"Error: {e}")
                        except ET.ParseError as e:
                            print(Fore.RED + f"XML Parse Error: {e}")

                    elif action == "10":
                        api_url = input(Fore.WHITE + "Enter JSON API URL: ")
                        try:
                            response = requests.get(api_url)
                            response.raise_for_status()
                            print(Fore.WHITE + "JSON Response:")
                            print(json.dumps(response.json(), indent=4))
                        except requests.exceptions.RequestException as e:
                            print(Fore.RED + f"Error: {e}")
                        except json.JSONDecodeError as e:
                            print(Fore.RED + f"JSON Decode Error: {e}")

                    elif action == "11":
                        print(Fore.WHITE + "Simulating API Rate Limit...")
                        import time
                        try:
                            api_url = input(Fore.WHITE + "Enter API URL: ")
                            requests_per_minute = int(input(Fore.WHITE + "Enter maximum requests per minute: "))
                            delay = 60 / requests_per_minute
                            for i in range(requests_per_minute + 5):
                                start_time = time.time()
                                try:
                                    response = requests.get(api_url)
                                    response.raise_for_status()
                                    print(Fore.GREEN + f"Request {i + 1}: Status {response.status_code}")
                                except requests.exceptions.RequestException as e:
                                    print(Fore.RED + f"Request {i + 1}: Error - {e}")
                                time_taken = time.time() - start_time
                                sleep_time = max(0, delay - time_taken)
                                time.sleep(sleep_time)
                            print(Fore.WHITE + "Rate limit simulation complete.")
                        except ValueError:
                            print(Fore.RED + "Invalid input for requests per minute.")


                    elif action in ("12", "13", "14", "15", "16", "17"):
                        print(Fore.YELLOW + "Feature not implemented yet.")

                    else:
                        print(Fore.RED + "Invalid action.")

                except Exception as e:
                    print(Fore.RED + f"An unexpected error occurred in action_process: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)
            
            def show_menu(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color+self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(Fore.WHITE+"  - Welcome to the API Tester!")
                print(
                    """
 [0] Exit API Tester             [6] Send PUT Request             [12] Test API Security
 [1] API PING                    [7] Send DELETE Request          [13] Test Webhook Integration
 [2] Check API Status            [8] Send DELETE Request          [14] Monitor API Usage
 [3] Send GET Request            [9] Fetch Data in XML Format     [15] Validate API Schema
 [4] Send POST Request           [10] Fetch Data in JSON Format   [16] Test Pagination
 [5] Test API Authentication     [11] Simulate API Rate Limit     [17] Mock API Requests

""")
                try:
                    action = input(Fore.WHITE+" >>> ").strip().lower()
                    SXServiseCLI.System.api.action_process(self, action)
                except Exception as e:
                    print(Fore.RED+f"An unexpected error occurred.")
                    logging.error(f"Component API: An unexpected error occurred: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)
                    
            def run(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color+self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(Fore.WHITE+" Welcome to SXSCLI:API!")
                logging.info("Component API: Successfully launched.")
                try:
                    print(Fore.WHITE+" ")
                    SXServiseCLI.System.api.show_menu(self)
                except Exception as e:
                    print(Fore.RED+"Error: Component API failed to start.")
                    logging.error(f"Component API: Error: {e}")
                finally:
                    SXServiseCLI.System.run_input(self)
        
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
                            console=self.console
                            print(f"Successful connection to the FTP server")
                            console.print(Panel("[bold cyan]FTP[/bold cyan]"))
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
                    
        def about(self):
            print(Fore.WHITE+" About SXServiseCLI:")
            print(Fore.WHITE+
""" SXServiseCLI 2024 - is a powerful and versatile command-line tool that helps you 
 run local services, generate JSON files, create QR codes, test APIs, SSH, FTP, 
 and much more.

 WIKI: https://github.com/StasX-Official/SXServiseCLI/wiki
 GitHub: https://github.com/StasX-Official/SXServiseCLI
""")
            SXServiseCLI.System.run_input(self)
                 
        class SSH:
            def _get_completer(self):
                commands = [
                    "help", "exit", "ls", "pwd", "whoami", "df", "uptime", "free", "uname", "top",
                    "date", "df -i", "grep", "find", "cat", "head", "tail", "man", "chmod", "chown",
                    "ps", "kill", "tar", "df -h", "lsof", "history", "ifconfig", "ip", "netstat",
                    "ssh-keygen", "curl", "wget", "top -o", "df -T", "du", "dd", "lsblk", "mount",
                    "umount", "systemctl", "journalctl", "crontab", "rsync", "chmod +x", "stat",
                    "df -hT", "du -sh", "find /path -exec cmd {} \\;", "du -a", "sort", "awk", "sed",
                    "head -n", "tail -n", "wget -O", "curl -o", "touch", "echo", "diff", "file",
                    "xargs", "gzip", "gunzip", "bzip2", "bunzip2", "mkdir", "rm", "mv", "cp", "alias",
                    "unalias", "hostname", "traceroute", "ping", "df -h --total", "ssh-copy-id", "nano",
                    "vim", "du -m", "tree", "locate", "last", "uptime -p", "uptime -s", "dmesg",
                    "clear", "tac", "ln", "shutdown", "reboot"
                ]
                return WordCompleter(commands, ignore_case=True)

            def _get_key_bindings(self):
                bindings = KeyBindings()

                @bindings.add('c-c')
                def _(event):
                    event.app.exit()
                return bindings

            def _get_style(self):
                return Style.from_dict({
                    'prompt': self.input_color,
                    'completion-menu.completion': 'bg:#0088aa #ffffff',
                    'completion-menu.completion.current': 'bg:#bbddff #000000',
                    'scrollbar.background': 'bg:#88aaaa',
                    'scrollbar.button': 'bg:#222222',
                })

            def _display_help(self):
                help_text = """Available commands:
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
        """
                print(Fore.LIGHTGREEN_EX + help_text)



            def _get_user_input(self, prompt):
                return self.session.prompt(prompt)


            def run(self):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.logo_color + self.logo)
                print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                print(" ")
                print(Fore.WHITE + " Welcome to SXSCLI:SSH!")
                logging.info("Component SSH: Successfully launched.")
                print(" ")
                initial_choice = self._get_user_input(Fore.WHITE + "Do you want to continue? (connect/exit) >>> ").lower()

                if initial_choice == "exit" or ssh_status == False:
                    SXServiseCLI.System.run_input(self)
                    return

                ssh_host = SXServiseCLI.System.SSH._get_user_input(self.input_color + " - Enter SSH Host: ")
                ssh_username = SXServiseCLI.System.SSH._get_user_input(self.input_color + " - Enter SSH Username: ")
                ssh_password = input(Fore.WHITE + " - Enter SSH Password: ")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                try:
                    ssh.connect(ssh_host, username=ssh_username, password=ssh_password)
                    print(Fore.LIGHTGREEN_EX + f"Successful connection to {ssh_host}\n")
                    self.console.print(Panel("[bold cyan]SSH[/bold cyan]"))
                    logging.info(f"SSH: Successful connection to {ssh_host}")

                    while True:
                        command = self._get_user_input(self.input_color + "Enter the command (or 'help' for available commands, 'exit' to quit): ")
                        logging.info(f"SSH: The user launched the command: {command}")

                        if command.lower() == "exit":
                            break

                        elif command.lower() == "help":
                            self._display_help()
                            continue

                        command_actions = {
                            "mkdir": ("Enter directory name to create: ", lambda x: f"mkdir {x}"),
                            "rm": ("Enter file or directory to remove: ", lambda x: f"rm -r {x}"),
                            "mv": ("Enter source file or directory: ", lambda x, y: f"mv {x} {y}", "Enter destination: "),
                            "cp": ("Enter source file or directory: ", lambda x, y: f"cp -r {x} {y}", "Enter destination: "),
                            "alias": ("Enter alias command: ", lambda x: f"alias {x}"),
                            "unalias": ("Enter alias to remove: ", lambda x: f"unalias {x}"),
                            "hostname": (None, lambda: "hostname"),
                            "traceroute": ("Enter target host: ", lambda x: f"traceroute {x}"),
                            "ping": ("Enter target host: ", lambda x: f"ping -c 4 {x}"),
                            "df -h --total": (None, lambda: "df -h --total"),
                            "ssh-copy-id": ("Enter user@host: ", lambda x: f"ssh-copy-id {x}"),
                            "nano": ("Enter file to edit: ", lambda x: f"nano {x}"),
                            "vim": ("Enter file to edit: ", lambda x: f"vim {x}"),
                            "du -m": ("Enter directory to check usage: ", lambda x: f"du -m {x}"),
                            "tree": (None, lambda: "tree"),
                            "locate": ("Enter filename to locate: ", lambda x: f"locate {x}"),
                            "last": (None, lambda: "last"),
                            "uptime -p": (None, lambda: "uptime -p"),
                            "uptime -s": (None, lambda: "uptime -s"),
                            "dmesg": (None, lambda: "dmesg"),
                            "clear": (None, lambda: "clear"),
                            "ln": ("Enter target file: ", lambda x, y: f"ln -s {x} {y}", "Enter name for the link: "),
                            "shutdown": (None, lambda: "shutdown now"),
                            "reboot": (None, lambda: "reboot"),
                            "ls": (None, lambda: "ls -la"),
                            "pwd": (None, lambda: "pwd"),
                            "whoami": (None, lambda: "whoami"),
                            "df": (None, lambda: "df -h"),
                            "uptime": (None, lambda: "uptime"),
                            "free": (None, lambda: "free -h"),
                            "uname": (None, lambda: "uname -a"),
                            "top": (None, lambda: "top -bn1"),
                            "date": (None, lambda: "date"),
                            "df -i": (None, lambda: "df -i"),
                            "grep": ("Enter pattern to search: ", lambda x, y: f"grep '{x}' {y}", "Enter file to search in: "),
                            "find": ("Enter directory to search in: ", lambda x, y: f"find {x} -name {y}", "Enter file or pattern to search for: "),
                            "cat": ("Enter file to display: ", lambda x: f"cat {x}"),
                            "head": ("Enter file to display: ", lambda x, y: f"head -n {y} {x}", "Enter number of lines to display: "),
                            "tail": ("Enter file to display: ", lambda x, y: f"tail -n {y} {x}", "Enter number of lines to display: "),
                            "man": ("Enter command to display manual: ", lambda x: f"man {x}"),
                            "chmod": ("Enter permissions (e.g., 755): ", lambda x, y: f"chmod {x} {y}", "Enter file to change permissions: "),
                            "chown": ("Enter new owner: ", lambda x, y: f"chown {x} {y}", "Enter file to change owner: "),
                            "ps": (None, lambda: "ps aux"),
                            "kill": ("Enter process ID to kill: ", lambda x: f"kill {x}"),
                            "tar": ("Enter tar options (e.g., -czvf): ", lambda x, y, z: f"tar {x} {y} {z}", "Enter archive name: ", "Enter files to archive: "),
                            "lsof": (None, lambda: "lsof"),
                            "history": (None, lambda: "history"),
                            "ifconfig": (None, lambda: "ifconfig"),
                            "ip": (None, lambda: "ip a"),
                            "netstat": (None, lambda: "netstat -tuln"),
                            "curl": ("Enter URL: ", lambda x: f"curl {x}"),
                            "wget": ("Enter URL: ", lambda x: f"wget {x}"),
                            "top -o": ("Enter field to sort by (e.g., %MEM): ", lambda x: f"top -o {x}"),
                            "df -T": (None, lambda: "df -T"),
                            "du": ("Enter directory to check usage: ", lambda x: f"du -sh {x}"),
                            "touch": ("Enter file to create or update: ", lambda x: f"touch {x}"),
                            "echo": ("Enter text to display: ", lambda x: f"echo {x}"),
                            "diff": ("Enter first file to compare: ", lambda x, y: f"diff {x} {y}", "Enter second file to compare: "),
                            "file": ("Enter file to determine type: ", lambda x: f"file {x}"),
                            "xargs": ("Enter command to execute: ", lambda x: f"xargs {x}"),
                            "gzip": ("Enter file to compress: ", lambda x: f"gzip {x}"),
                            "gunzip": ("Enter file to decompress: ", lambda x: f"gunzip {x}"),
                            "bzip2": ("Enter file to compress: ", lambda x: f"bzip2 {x}"),
                            "bunzip2": ("Enter file to decompress: ", lambda x: f"bunzip2 {x}")
                        }

                        if command.lower() in command_actions:
                            action = command_actions[command.lower()]
                            if action[0] is None:
                                final_command = action[1]()
                            elif len(action) == 3:
                                arg1 = SXServiseCLI.System.SSH._get_user_input(Fore.LIGHTGREEN_EX + action[0])
                                arg2 = SXServiseCLI.System.SSH._get_user_input(Fore.LIGHTGREEN_EX + action[2])
                                final_command = action[1](arg1, arg2)
                            elif len(action) == 4:
                                arg1 = SXServiseCLI.System.SSH._get_user_input(Fore.LIGHTGREEN_EX + action[0])
                                arg2 = SXServiseCLI.System.SSH._get_user_input(Fore.LIGHTGREEN_EX + action[2])
                                arg3 = SXServiseCLI.System.SSH._get_user_input(Fore.LIGHTGREEN_EX + action[3])
                                final_command = action[1](arg1, arg2, arg3)
                            else:
                                arg = SXServiseCLI.System.SSH._get_user_input(Fore.LIGHTGREEN_EX + action[0])
                                final_command = action[1](arg)

                        else:
                            final_command = command

                        stdin, stdout, stderr = ssh.exec_command(final_command)
                        output = stdout.read().decode("utf-8")
                        error = stderr.read().decode("utf-8")

                        if output:
                            print(Fore.LIGHTGREEN_EX + output)
                            logging.info(f"SSH: The component provided the response: {output}")
                        if error:
                            print(Fore.RED + error)
                            logging.error(f"SSH: The component has given an error: {error}")

                except Exception as e:
                    print(self.errors_color + f"Error connecting to the SSH server: {e}")
                    print(" ")
                    logging.error(f"Error connecting to the SSH server: {e}")
                    try:
                        SXServiseCLI.System.run_input(self) 
                    except NameError:
                        print("Error: SXServiseCLI.System is not defined.")

                finally:
                    print(" ")
                    try:
                        SXServiseCLI.System.run_input(self) 
                    except NameError:
                        print("Error: SXServiseCLI.System is not defined.")
        
        def run_command(self, command):
            logging.info("Launching the component: Entering the command")
            try:
                if command.lower() == "exit":
                    time.sleep(1)
                    sys.exit()
                elif command.lower() == "ssh":
                    SXServiseCLI.System.SSH.run(self)
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
                elif command.lower() == "genai":
                    SXServiseCLI.System.AI.genai_google.run(self)
                elif command.lower() == "device":
                    SXServiseCLI.System.device.run(self)
                elif command.lower() == "faker":
                    SXServiseCLI.System.faker.run(self)
                elif command.lower() == "netmon":
                    SXServiseCLI.System.netmon.run(self)
                elif command.lower() == "ai":
                    SXServiseCLI.System.ai(self)
                elif command.lower() == "db":
                    SXServiseCLI.System.db.run(self)
                elif command.lower() == "networkinfo":
                    SXServiseCLI.System.networkinfo.run(self)
                elif command.lower() == "about":
                    SXServiseCLI.System.about(self)
                elif command.lower() == "qrcode":
                    SXServiseCLI.System.qrcode.run(self)
                elif command.lower() == "api":
                    SXServiseCLI.System.api.run(self)
                elif command.lower() == "speedtest":
                    SXServiseCLI.System.check_speed(self)
                elif command.lower() == "cpu":
                    SXServiseCLI.System.get_cpu_info(self)
                elif command.lower() == "gpu":
                    SXServiseCLI.System.get_gpu_info(self)
                elif command.lower() == "status":
                    SXServiseCLI.System.status(self)
                elif command.lower() == "mediapipe":
                    SXServiseCLI.System.AI.mediapipe.run(self)
                    
                elif command.lower() == "ip":
                    local_ip=sxscli_core.System.Actions.get_local_ip(self=0)
                    print(Fore.WHITE+f" - Your local IP: {local_ip}")
                    public_ip=sxscli_core.System.Actions.get_public_ip(self=0)
                    print(Fore.WHITE+f" - Your public IP: {public_ip}")
                    SXServiseCLI.System.run_input(self)
                
                elif command.lower() == "clear":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.logo_color+self.logo)
                    print(self.startmenu_color + f"                                                                                             {self.app_version}\n" if self.show_version else "", end="")
                    print(" ")
                    SXServiseCLI.System.run_input(self)
                
                elif command.lower() == "mac":
                    mac = sxscli_core.System.Actions.get_mac_address(self=0)
                    print(Fore.WHITE+f" - Your MAC address: {mac}")
                    SXServiseCLI.System.run_input(self)
                
                elif command.lower() == ".":
                    f_size = sum(os.path.getsize(os.path.join(root, file)) for root, dirs, files in os.walk("Staff/logs") for file in files) / 1024
                    if str(input(Fore.WHITE+f" - Are you sure you want to clear the logs? {f_size} KB (y/n): ")).lower()=="y":
                        for root, dirs, files in os.walk("Staff/logs", topdown=False):
                            for file in files:
                                os.remove(os.path.join(root, file))
                            for dir in dirs:
                                shutil.rmtree(os.path.join(root, dir)) 
                        print(" ")
                        SXServiseCLI.System.run_input(self)
                    else:
                        print(" ")
                        SXServiseCLI.System.run_input(self)

                elif re.match(r"^search (.*)", command.lower()):
                    SXServiseCLI.System.Search(self, promt=re.match(r"^search (.*)", command.lower()).group(1).capitalize())
                
                else:
                    print(self.errors_color+" - 404. Command not found. Command list: help")
                    logging.error(f"404. Command: {command} not found.")
                    SXServiseCLI.System.run_input(self)
            except Exception as e:
                print(self.errors_color+f" - Error: {e}")
                logging.error(f"Error: {e}")
                SXServiseCLI.System.run_input(self)
        
        def run_input(self):
            try:
                if self.sxscli_completer_status:
                    cmd = prompt(" $ >>> ", completer=self.completer)
                    SXServiseCLI.System.run_command(self, command=cmd) 
                else:
                    cmd = input(f"{self.input_color} $ >>> ")
                    SXServiseCLI.System.run_command(self, command=cmd) 
            except Exception as e:
                print(self.errors_color + " - Input command error. ")
                logging.critical(f"Input command error: {e}")
                time.sleep(5)
                sys.exit()