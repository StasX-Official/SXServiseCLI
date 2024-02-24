def sxg_save_log(error_code, error_txt):
    from datetime import datetime
    file = open("logs.txt", "a")
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    text_to_write = f"{formatted_time}" + "Error code: " + error_code + error_txt + "ERROR\n"
    file.write(text_to_write)
    file.close()