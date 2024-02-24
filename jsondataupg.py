import json

def appdata():
    with open('sxserviseclidata.json') as f:
        data = json.load(f)  

    # Дістаємо дані з JSON і записуємо в змінні
    app_name = data["appName"]
    version = data["version"]
    app_id = data["id"]
    com = data["com"]
    author = data["author"]
    description = data["description"]
    license = data["license"]
    ai_support = data["settings"]["ai_support"]
    api_enabled = data["settings"]["api"]
    api_path = data["settings"]["api_path"]
    logs_enabled = data["settings"]["logs"]
    username = data["user_info"]["username"]
    password = data["user_info"]["password"]
    mail = data["user_info"]["mail"]
    
    local_default_port = data["local_host"]["default_port"]
    local_hosting_support = data["local_host"]["local_hosting_support"]
    local_default_path = data["local_host"]["default_path"]
    
    

    # Повертаємо змінні з даними
    return app_name, version, app_id, com, author, description, license, api_enabled, api_path, logs_enabled, username, password, mail, ai_support, local_default_port, local_hosting_support, local_default_path

# Викликаємо функцію та отримуємо дані
app_name, version, app_id, com, author, description, license, api_enabled, api_path, logs_enabled, username, password, mail, ai_support, local_default_port, local_hosting_support, local_default_path = appdata()
