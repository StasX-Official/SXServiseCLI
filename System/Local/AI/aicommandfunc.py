#You currently have access to the license file that is required to use AI in SXServiseCLI, as this is a beta version.
#Any action related to viewing, changing, modifying, distributing, etc. of this file is illegal and violates SX rules
#Please do not violate the rules above, it is prohibited by SX rules.


def aifuncc():
    print(" ")
    print("To get beta access to SXServiseCLI AI, you need to login.")
    print(" ")
    print("Continue - 0")
    print("Exit - 1")
    print(" ")
    eref = int(input(">>> "))
    aifuncauth(eref)
    
def aifuncauth(code):
    if code == 0:
        print(" ")
        print("/1-3/ Enter the license key: (SXAI-0000-0000-0000-Q)")
        licensekeyai = input(">>> ")
        print(" ")
        
        print("/2-3/Enter security code: (00-00-00-00)")
        securitykeyai = input(">>> ")
        print(" ")
        
        print("/3-3/Enter you mail: (**********@mail.com)")
        usermail = input(">>> ")
        print(" ")
        
        betalicense(licensekeyai, securitykeyai, usermail)
        
        
    elif code == 1:
        print("Restarting...")
    else:
        print("Error 404.")
        aifuncc()
        
def betalicense(licensekeyai0, securitykeyai0, usermail):
    import time
    global license
    license = "SXAI-6014-2328-7091-Q"
    global securitykey
    securitykey = "76-96-26-77"
    if licensekeyai0 == license:
        print("Correct license key.")
        time.sleep(2)
        if securitykeyai0 == securitykey:
            print("Correct security key.")
    else:
        print("Dont correct license key.")

aifuncc()
        