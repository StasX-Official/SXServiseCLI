#SXServiseCLI API CORE

global api_status

def core_sxservise_api(code, metod, data, api_path):
    global api_status
    if code == 0: #TEST_API
        pass
    elif code == 1: #SEND_DATA
        pass
    elif code == 2: #GET_DATA
        pass
    elif code == 3: #START_API
        
        api_status = True
        
        return api_status
    elif code == 4: #STOP_API
        
        api_status = False
        
        return api_status
    elif code == 8:
        return api_status     
    else:
        return "Error to CODE data."