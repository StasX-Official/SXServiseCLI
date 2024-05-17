
def core_main(code, data):
    #Запуск програм
    if code == 0: #STOP_CORE
        if data == 1:
            from System.Local.sxg.cors.sxg_servises_core import core_sxservise_api
            status = core_sxservise_api(4, 0, 0, 0)
            print(status)
    elif code == 1: #START_CORE
        if data == 0:
            from System.Local.sxg.cors.sxg_servises_core import core_sxservise_api
            status = core_sxservise_api(3, 0, 0, 0)
            print(status)
    elif code == 3: #GET_CORE_INFO - STATUS
        if data == 0: #GET_ALL_CORE_INFO
            from System.Local.sxg.cors.sxg_servises_core import core_sxservise_api
            status = core_sxservise_api(8, 0, 0, 0)
            if status == False:
                return False
            elif status == True:
                return True
            else:
                return "ERROR"
        else:
            return "Error data_st"
    else:
        return "Error to code_data."




def core_init():
    
    #root_init
    #ROOT USER NAME
    root_name="sxservisecli1"
    #ROOT USER PASS
    root_pass="sxservisecli1"
    return root_name, root_pass

    

def core_command_auth():
    pass

def core_user_auth(user_name,user_passworld,user_mail):
    core_user_info=user_name
    core_user_password=user_passworld
    core_user_mail=user_mail
    
    user = [core_user_info, core_user_mail, core_user_password]

    

root_name, root_pass = core_init()

#core_main(1,0) #Запуск ядра сервісу
#servisecore_st = core_main(3,0) #Перевірка ядра сервісу
#print(servisecore_st) 
