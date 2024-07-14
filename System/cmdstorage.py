class sxservisecli2024:
    class system:
        def __init__(self):
            project_id=int(data.pop("project_id"))
            app_id=str(data.pop("app_id"))
            key=int(data.pop("key"))
            secret=str(data.pop("secret"))
            logs=bool(data.pop("logs"))
            model=str(data.pop("model"))
            root=bool(data.pop("root"))
            root_name=str(data.pop("root_name"))
            root_password=str(data.pop("root_pass"))
            global root_status
            
            if logs==True:
                #INIT
                if model=="sxservisecli-01-global":
                    print("LOGS: Model activated.")
                    #ROOT_CHEAK
                    if root==True:
                        if root_name=="sxservisecli1":
                            print("LOGS: ROOT_NAME -> TRUE")
                            if root_password=="sxservisecli1":
                                print("LOGS: ROOT_PASS -> TRUE")
                                print("LOGS: ROOT -> TRUE")
                                root_status=True
                            else:
                                print("LOGS: ROOT_PASS -> FALSE")
                                root_status=False
                        else:
                            print("LOGS: ROOT_NAME -> FALSE")
                            root_status=False
                    #AUTH
                    import json
                    with open("my_project.json", "r") as project_t:
                        data_js = json.load(project_t)
                    Dproject_id=data_js["Project_ID"]
                    Dapp_id=data_js["App_ID"]
                    Dkey=data_js["Key"]
                    Dsecret=data_js["Secret"]
                    if project_id==Dproject_id:
                        print("AUTH_LOGS: 1/4 TRUE")
                        if Dapp_id==app_id:
                            print("AUTH_LOGS: 2/4 TRUE")
                            if key==Dkey:
                                print("AUTH_LOGS: 4/4 TRUE")
                                if secret==Dsecret:
                                    return True
                            else:
                                print("AUTH_LOGS: FALSE. Critical error 404.")
                                return False
                        else:
                            print("AUTH_LOGS: FALSE. Critical error 404.")
                            return False
                    else:
                        print("AUTH_LOGS: FALSE. Critical error 404.")
                        return False
                else:
                    print("LOGS: Error initializing the model. Model not found. Critical error 404.")
                    return False
            
            print("project_id:", project_id)
            print("app_id:", app_id)
            print("key:", key)
            print("secret:", secret)
            print("logs:", logs)
            print("model:", model)
            print("root:", root)
            print("root_name:", root_name)
            


data={
    "project_id": 0000,
    "app_id": "TEST",
    "key": 0000,
    "secret": "TEST",
    "logs":True,
    "model":"sxservisecli-01-global",
    "root":True,
    "root_name":"",
    "root_pass":""
    
}

x=sxservisecli2024.system.__init__(data)
print(x)

#TEST!!! NOT OFFICIAL!!
