import os
global mods_dir_path
mods_dir_path="Mods"

def scan_mods():
    mods = []
    try:
        for entry in os.listdir(mods_dir_path):
            if os.path.isdir(os.path.join(mods_dir_path, entry)):
                mods.append(entry)
    except FileNotFoundError:
        print(f"Folder '{mods_dir_path}' not found.")
    return mods

def mods_menu():
    print("==========================================")
    print("SXServiseCLI 2024. Mods: ")
    print("==========================================")
    print("Mods: ")
    mods = scan_mods()
    for i, mod in enumerate(mods):
        print(f"{i}. {mod}")
    
    print("What mod should we run?")
    fd = int(input("Enter the mod number >>> "))
    trt = input("Run the mod? t/f: ")
    
    if trt == "t":
        selected_mod = mods[fd]
        # Тут можна додати код для запуску обраного модуля
        print(f"Running the mod: {selected_mod}")
    elif trt == "f":
        print("Cancel launch...")
    else:
        print("Error. Wrong answer.")
        
mods_menu()
