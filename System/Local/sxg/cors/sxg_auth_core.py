def sxg_core_main(logs_en, command):
    global core_power
    core_power=False
    #AUTH CORE MAIN
    global logs
    logs = logs_en
    if command=="start":
        core(1,"test")
    elif command=="stop":
        core(0,"test")
    elif command=="restart":
        core(2,"test")
    else:
        return "ERROR! COR: sxg_auth_core. ERROR: Wrong command."

def core(core_command,cmd):
    def core_control(command):
        if command==1:
            if logs==True:
                print("COR: sxg_auth_core. COMM: Launch!")
                core_sys_start()
            else:
                core_sys_start()
        elif command==0:
            if logs==True:
                print("COR: sxg_auth_core. COMM: Stop!")
                core_sys_stop()
            else:
                core_sys_stop()
        elif command==2:
            if logs==True:
                print("COR: sxg_auth_core. COMM: Restart!")
                core_sys_rst()
            else:
                core_sys_rst()
        else:
            return "ERROR! COR: sxg_auth_core. ERROR: Wrong command."
    
    def core_sys(cmd):
        if cmd=="stop":
            if logs==True:
                print("COR: sxg_auth_core. COMM: STOP -> TRUE!")
                core_power = False
            else:
                core_power = False
        elif cmd=="start":
            if logs==True:
                print("COR: sxg_auth_core. COMM: RUNNING -> TRUE.")
                core_power = True
            else:
                core_power = True
        
        elif core_power==True:
            if logs==True:
                print("COR: sxg_auth_core. COMM: No problems found. Core: Running!")
                
            def authenticate_user():
                pass
        elif core_power==False:
            return "ERROR! COR: sxg_auth_core. ERROR: COR_DISABLED!"
    core_sys(cmd)

        
    
    def core_sys_rst():
        core_command()
    
    def core_sys_stop():
        core_sys("stop")
        
    def core_sys_start():
        core_sys("start")
    
    core_control(core_command)