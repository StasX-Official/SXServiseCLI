import sys, time
try:
    from System.sxscli_web_core import AI_WITH_WEB_INTERFACE
    ai_interface = AI_WITH_WEB_INTERFACE()
    ai_interface.start()
except Exception as e:
    print(f"Error: {e}")
    time.sleep(2)
    sys.exit()