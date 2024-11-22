import uuid
import platform
import requests
import socket
import psutil
import json

class System:
    def __init__(self):
        pass
    
    class sxscli:
        def get_version(self):
            with open("System\configs\system.cfg.json", "r") as f:
                data = json.load(f)
                return data['version']
        
        def get_com(self):
            with open("System\configs\system.cfg.json", "r") as f:
                data = json.load(f)
                return data['com']
        
        def get_api_path(self):
            with open("System\configs\system.cfg.json", "r") as f:
                data = json.load(f)
                return data["settings"]['api_path']
        
        def get_settings(self):
            with open("System\configs\system.cfg.json", "r") as f:
                data = json.load(f)
                return data["settings"]
        
        def get_id(self):
            with open("System\configs\system.cfg.json", "r") as f:
                data = json.load(f)
                return data["id"]
            
        def get_database_path(self):
            with open("System\configs\system.cfg.json", "r") as f:
                data = json.load(f)
                return data["settings"]["database_path"]
    
    class Actions:
        def get_mac_address(self):
            mac = uuid.getnode()
            mac_address = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
            return mac_address
        
        def get_global_system_info(self):
            info = {
                "System": platform.system(),
                "Node Name": platform.node(),
                "Release": platform.release(),
                "Version": platform.version(),
                "Machine": platform.machine(),
                "Processor": platform.processor()
            }
            return info

        def get_public_ip(self):
            response = requests.get("https://api.ipify.org?format=json")
            ip_data = response.json()
            return ip_data['ip']
        
        def get_local_ip(self):
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return local_ip
        
        def get_disk_info(self):
            partitions = psutil.disk_partitions()
            disk_info = {}
            
            for partition in partitions:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info[partition.device] = {
                    "mount_point": partition.mountpoint,
                    "file_system_type": partition.fstype,
                    "total_size": usage.total,
                    "used": usage.used,
                    "free": usage.free,
                    "usage_percent": usage.percent
                }
            return disk_info