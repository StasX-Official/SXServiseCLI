from System.main import SXServiseCLI
from System.commands_map import commands_map
import argparse, os, sys, ctypes, json, winreg, platform

def is_admin(): return ctypes.windll.shell32.IsUserAnAdmin() != 0 if sys.platform == "win32" else False

def add_to_path():
    p = os.path.dirname(os.path.abspath(__file__))
    if sys.platform == "win32":
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_SET_VALUE) as k:
                v = winreg.QueryValueEx(k, "Path")[0]
                if p not in v:
                    winreg.SetValueEx(k, "Path", 0, winreg.REG_EXPAND_SZ, f"{v};{p}")
                    os.system("taskkill /f /im explorer.exe && start explorer.exe")
        except: pass
    elif sys.platform == "linux":
        try:
            if data.get("add_to_path_linux_", False):
                with open(os.path.expanduser("~/.bashrc"), "a") as bashrc: 
                    bashrc.write(f'\nexport PATH="$PATH:{p}"\n')
        except: pass
    else:
        pass

try:
    with open("System/configs/control.json", "r") as f:
        data = json.load(f)
    data.setdefault("add_to_path_linux_", False)
    admin_rights = is_admin() if data.get("check_admin_rights_", False) else True
    if data.get("add_to_path_windows_", False) and sys.platform == "win32" and admin_rights:
        add_to_path()
    elif sys.platform == "linux" and data.get("add_to_path_linux_", False):
        add_to_path()
    parser = argparse.ArgumentParser(description="SXServiseCLI 2024")
    parser.add_argument('command', type=str, help='Command (e.g., help)')
    os.system('cls' if os.name == 'nt' else 'clear')
    args = parser.parse_args()
    SXServiseCLI(other=commands_map.get(args.command, "run"), admin_rights=admin_rights)
except: SXServiseCLI("run", admin_rights=admin_rights)
