import json
def appdata():
    with open('sxserviseclidata.json') as f:
        data_load = json.load(f)
    
    data={
        "Auth_Control_API_path": data_load["app_api_settings"]["Auth_Control_API_path"],
        "Version_Control_API_path": data_load["app_api_settings"]["Version_Control_API_path"],
        "Cloud_Control_API_path": data_load["app_api_settings"]["Cloud_Control_API_path"],
        "Analytics_Control_API_path": data_load["app_api_settings"]["Analytics_Control_API_path"],
        "Servise_Status_API_path": data_load["app_api_settings"]["Servise_Status_API_path"],
        "Settings":{
            "Security":{
                "AUTH":data_load["app_api_settings"]["Settings"]["Security"]["AUTH"],
                "SSL":data_load["app_api_settings"]["Settings"]["Security"]["SSL"]
            },
            "MetodsSupport":{
                "GET":data_load["app_api_settings"]["Settings"]["MetodsSupport"]["GET"],
                "POST":data_load["app_api_settings"]["Settings"]["MetodsSupport"]["POST"],
                "PUT":data_load["app_api_settings"]["Settings"]["MetodsSupport"]["PUT"],
                "DELETE":data_load["app_api_settings"]["Settings"]["MetodsSupport"]["DELETE"],
                "Others":data_load["app_api_settings"]["Settings"]["MetodsSupport"]["Others"]
            },
            "API_STATUSES_LOGGINING":data_load["app_api_settings"]["Settings"]["API_STATUSES_LOGGINING"]
        }
    }
    return data
apidata=appdata()
