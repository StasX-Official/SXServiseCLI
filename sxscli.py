from System.main import SXServiseCLI
from System.commands_map import commands_map
import argparse,os
try:
    parser = argparse.ArgumentParser(
        description="SXServiseCLI 2024 - is a powerful and versatile command-line tool that helps you run local services, generate JSON files, create QR codes, test APIs, SSH, FTP, and much more."
    )
    parser.add_argument('command', type=str, help='Command, ex.: ssh')
    os.system('cls' if os.name == 'nt' else 'clear')
    args = parser.parse_args()

    command_to_run = commands_map.get(args.command, "run")
    SXServiseCLI(other=command_to_run)
except:
    SXServiseCLI("run")

#python sxscli.py ***