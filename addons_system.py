import json

def appdata():
    with open('sxserviseclidata.json') as f:
        data = json.load(f)

    addons_data = {
        "addons_support_status": data["app_addons"]["addons_support_status"],
        "addons_user_auth_system_status": data["app_addons"]["addons_user_auth_system_status"],
        "addons_need_user_plan_to_run": data["app_addons"]["addons_need_user_plan_to_run"],
        "SXSC-Security": {
            "addons_pack_name": data["app_addons"]["SXSC-Security"]["addons_pack_name"],
            "addon_pack_id": data["app_addons"]["SXSC-Security"]["addon_pack_id"],
            "addons_pack_version": data["app_addons"]["SXSC-Security"]["addons_pack_version"],
            "addons_pack_path": data["app_addons"]["SXSC-Security"]["addons_pack_path"],
            "addons_pack_status_active": data["app_addons"]["SXSC-Security"]["addons_pack_status_active"]
        },
        "SXSC-Analytics": {
            "addons_pack_name": data["app_addons"]["SXSC-Analytics"]["addons_pack_name"],
            "addon_pack_id": data["app_addons"]["SXSC-Analytics"]["addon_pack_id"],
            "addons_pack_version": data["app_addons"]["SXSC-Analytics"]["addons_pack_version"],
            "addons_pack_path": data["app_addons"]["SXSC-Analytics"]["addons_pack_path"],
            "addons_pack_status_active": data["app_addons"]["SXSC-Analytics"]["addons_pack_status_active"]
        },
        "SXSC-Optimizer": {
            "addons_pack_name": data["app_addons"]["SXSC-Optimizer"]["addons_pack_name"],
            "addon_pack_id": data["app_addons"]["SXSC-Optimizer"]["addon_pack_id"],
            "addons_pack_version": data["app_addons"]["SXSC-Optimizer"]["addons_pack_version"],
            "addons_pack_path": data["app_addons"]["SXSC-Optimizer"]["addons_pack_path"],
            "addons_pack_status_active": data["app_addons"]["SXSC-Optimizer"]["addons_pack_status_active"]
        },
        "SXSC-Monitoring": {
            "addons_pack_name": data["app_addons"]["SXSC-Monitoring"]["addons_pack_name"],
            "addon_pack_id": data["app_addons"]["SXSC-Monitoring"]["addon_pack_id"],
            "addons_pack_version": data["app_addons"]["SXSC-Monitoring"]["addons_pack_version"],
            "addons_pack_path": data["app_addons"]["SXSC-Monitoring"]["addons_pack_path"],
            "addons_pack_status_active": data["app_addons"]["SXSC-Monitoring"]["addons_pack_status_active"]
        },
        "SXSC-Integration": {
            "addons_pack_name": data["app_addons"]["SXSC-Integration"]["addons_pack_name"],
            "addon_pack_id": data["app_addons"]["SXSC-Integration"]["addon_pack_id"],
            "addons_pack_version": data["app_addons"]["SXSC-Integration"]["addons_pack_version"],
            "addons_pack_path": data["app_addons"]["SXSC-Integration"]["addons_pack_path"],
            "addons_pack_status_active": data["app_addons"]["SXSC-Integration"]["addons_pack_status_active"]
        },
        "SXSC-Storage": {
            "addons_pack_name": data["app_addons"]["SXSC-Storage"]["addons_pack_name"],
            "addon_pack_id": data["app_addons"]["SXSC-Storage"]["addon_pack_id"],
            "addons_pack_version": data["app_addons"]["SXSC-Storage"]["addons_pack_version"],
            "addons_pack_path": data["app_addons"]["SXSC-Storage"]["addons_pack_path"],
            "addons_pack_status_active": data["app_addons"]["SXSC-Storage"]["addons_pack_status_active"]
        }
    }
    return addons_data

addons_data_system=appdata()
