from System.main import SXServiseCLI
from System.commands_map import commands_map
try:
    import argparse
    parser = argparse.ArgumentParser(description="SXServiseCLI 2024 - is a powerful and versatile command-line tool that helps you run local services, generate JSON files, create QR codes, test APIs, SSH, FTP, and much more.")
    parser.add_argument('command', type=str, help='Command, ex.: ssh')
    args = parser.parse_args()

    SXServiseCLI(other=commands_map.get(args.command, "run"))
except:
    SXServiseCLI("run")

#python sxscli.py ***