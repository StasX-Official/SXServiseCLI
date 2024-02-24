import qrcode
import time
import tqdm
import os
from datetime import datetime
from colorama import init, Fore, Back, Style

current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
file = open("logs.txt", "a")

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

def command_qrcode_menu():
    print("--QrCode---")
    print("Create - 0")
    print("Edit Existing - 1")
    print("Decode - 2")
    print("Wi-Fi QR Code - 3")
    print("Exit   - 4")
    print("-----------")
    command_qrcode = int(input(Fore.BLUE + ">>> "))
    
    if command_qrcode == 0:
        create_qrcode()
    elif command_qrcode == 1:
        edit_qrcode()
    elif command_qrcode == 2:
        decode_qrcode()
    elif command_qrcode == 3:
        create_wifi_qrcode()
    elif command_qrcode == 4:
        text_to_write = f"{formatted_time} The exit command is running\n"
        file.write(text_to_write)
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        command_qrcode_menu()

    
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
        
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)

def decode_qrcode():
    print("Decode QR code:")
    qrcode_image = input("Enter the filename of the QR code image: ")
    
    try:
        img = qrcode.make(qrcode_image)
        qr_data = img.data.decode("utf-8")
        print("Decoded data:", qr_data)
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)
    except UnicodeDecodeError:
        print(Fore.RED + "Error decoding QR code." + Style.RESET_ALL)

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