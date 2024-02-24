#You currently have access to the license file that is required to use AI in SXServiseCLI, as this is a beta version.
#Any action related to viewing, changing, modifying, distributing, etc. of this file is illegal and violates SX rules
#Please do not violate the rules above, it is prohibited by SX rules.


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