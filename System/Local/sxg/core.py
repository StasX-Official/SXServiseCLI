def core_main():
    #Запуск програм
    pass



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
