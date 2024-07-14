import time
print("""
                        SXSERVISECLI2024
      УКРАЇНСЬКА:
      Привіт! Ви запустили меню налаштувань. 
      Якщо ви тільки перший раз запустили SXServiseCLI 
      вам потрібно заповнити деяку інформацію й налаштувати додаток.
      - - -
      English:
      Hello! You have launched the settings menu.
      If you are launching SXServiseCLI for the first time, 
      you need to fill in some information and configure the application.
      
      Виберіть мову:  choose a language:
      0 - Вийти (Exit)
      1 - Українська
      2 - English (Not available in beta build)
      
      @SXServiseCLI2024, StasX and SX. Copyright: MIT and STASX copyright.
      
      
      """)

def uk_version_st():
    print("""
          Ви запустили українську версію.
          Зараз ми налаштуємо додаток для вашого використання...
          Це буде відбуватись в 5 етапів.
          
          1- Згода з правилами
          2- Підтвердження
          3- Авторизація
          4- Налаштування функцій
          5- Видання ROOT прав
          
          Продовжимо? - y/n
          
          """)
    def p1():
        print("""
              Перший етап. Згода з правилами:
              1. Ви не можете використовувати SXServiseCLI для крадіжки, шахрайства, або інших незаконних дій.
              2. Ви при запуску цього додатку автомитично будете згодні з правилами. Якщо ви встановили цей додаток то ви теж автоматично згодні з правилами
              3. Якщо ви не згодні з правилами, то ви не можете використовувати SXServiseCLI.
              - Інші правила та політика на сайті або на вікіпедії додатку.
              - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
              Продовжити? y/n
            
              """)
        def p2():
            print("""
                  Другий етап. Підтвердження:
                  1. Ви підтверджуєте, згоду з правилами, політикою, авторським правом й правилами використання додатку.
                  2. Ви підтверджуєте й даєте згоду на обробку ваших данних (ІМЯ, ПОШТА, і тп.) 
                   - Ми не продаємо ваші данні.
                   - Ваші данні зашифрованні.
                  3. Ви підтверджуєте те, що ми не несемо відповідальність ща ваші дії. 
                  4. Ви підтверджуєте те, що ми маємо повне право не повертати кошти за підписку SXSERVISECLI+, SXSERVISECLI-PRO, й тд.
                   - Ми не надаємо повернення коштів.
                   - Ми можемо відмінити вашу підписку за порушення правил й заблокувати ваш аккаунт НАЗАВЖДИ.
                  5. Ви підтверджуєте те, що ми можемо змінити ці правила, політику, авторське право, правила використання тощо. 
                  6. Ви даєте дозвіл на зберігання регістраційних данних й те що ми не несемо за них відповідальність.
                  7. Ви підтверджуєте те, що програма має MIT ліцензію й ви це розумієте.
                  8. ЗАБОРОННЕНО! ДІЛИТИСЯ ІНФОРМАЦІЄЮ З ПЛАТНИХ* ВЕРСІЙ ДОДАТКУ! - БЛОКУВАННЯ IP ТА АККАУНТУ НАЗАВЖДИ!
                  9. Я згоден з іншими підтвердженнями які можуть бути на сайті або які були зміненні та доданні.
                  - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                  Продовжити? y/n
                    
                  
                  """)
            def p3():
                print("""
                      Третій етап. Авторизація:
                      
                      Як відбудеться авторизація?
                       - Ви створете аккаунт в цій програмі а потім такий самий на сайті
                       Для захисту потрібно регіструватись окремо але ОБОВЯЗКОВО звіряйте правильність введенних данних.
                       
                       Для регістьрації потрібно буде надати:
                        - Вашу пошту
                        - І'мя користувача
                        - Придумати пароль
                        - Ввести вік
                        
                        Вікове обменення: 16+ (Для захисту данних й пристрою)
                        - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                        Продовжити? y/n
                      """)
                def q6():
                    print("""
                          Останній етап:
                          Виберіть ліцензію:
                          1 - Ввести ліцензійний код (У мене він є)
                          2. У мене не має ліцензійного коду (Купити ліцензію)
                          3. Продовжити з безкоштовною версією 
                          """)
                    t=int(input("L >>> "))
                    if t==1:
                        print("""
                              Введіть ліцензійний ключ:
                              Приклад: 0000-0000-0000-0000-SXG
                              """)
                        key=input(">>> ")
                        pass
                    elif t==2:
                        print("""
                              Наразі для покупки можна використати:
                              1. Купити у телеграм боті (@sxserviseof_bot)
                              2. Напишіть на пошту (stasx.official.xx@gmail.com)
                              -> Повертайтесь коли у вас буде ліцензія...
                              """)
                        time.sleep(10)
                        exit()
                    elif t==3:
                        print("""
                              Продовжуємо з безкоштовною версією...
                              """)
                        global user_mail
                        global user_name
                        global user_pass
                        user_mail=user0_mail
                        user_name=user0_name
                        user_pass=user0_password
                        
                        import json
                        with open('sxserviseclidata.json', 'r') as r:
                            data = json.load(r)
                        data["user_info"]["username"] = user_name
                        data["user_info"]["password"] = user_pass
                        data["user_info"]["mail"] = user_mail
                        data["user_info"]["sxservisecliPlan_user"]="FREE"
                        print("1/2 TRUE")
                        with open('sxserviseclidata.json', 'w') as w:
                            json.dump(data, w, indent=4)
                        print("2/2 TRUE")
                        q7()
                    else:
                        print("Збій у роботі додатка...")
                        time.sleep(5)
                        exit()
                        
                def q7():
                    print("""
                          SXServiseCLI - Успішно налаштованно!
                          Для запуску програми запустіть файл: run.cmd (WINDOWS) SXServiseCLI.py (LINUX)
                          Гарного використання! :)
                          """)
                    time.sleep(5)
                    from jsondataupg import user1mail, user1name, sxservisecliPLUSuser, app_name, version, app_id, com, author, description, license, api_enabled, api_path, logs_enabled, ai_support, local_default_port, local_hosting_support, local_default_path
                    root_name = "sxservisecli1"
                    root_pass = "sxservisecli1"
                    from System.main import start_all
                    start_all(user1mail, user1name, sxservisecliPLUSuser, app_name, version, app_id, com, author, description, license, api_enabled, api_path, logs_enabled, ai_support, local_default_port, local_hosting_support, local_default_path, root_name, root_pass)
                                        
                def q5():
                    print("""
                          Пятий етап. Видання ROOT прав.
                          У деяких функціях додатку вам потрібно буде мати root доступ. Для цього вам портрібно:
                          
                          root_name - sxservisecli1
                          root_pass - sxservisecli1
                          
                          -> Рекомендуємо бути дуже обережними з root правами в SXServiseCLI. (Ми не несемо відповідальність за ваші дії.)
                          """)
                    q6()
                    
                def q4():
                    print("""
                          Четвертий етап. Налаштування.
                           - Ви можете змінити налаштування в будь-який час.
                           
                           -Як налаштувати? Для налаштування відкрийте sxserviseclidata.json й відредаруйте змінни.
                           - Що не можна змінювати? - API PATH. - НЕ ЗМІНЮВАТИ!
                           
                           Продовжити? y/n

                          """)
                    q133q=input(">>> ")
                    if q133q=="y":
                        q5()
                    elif q133q=="n":
                        print("Окей... Вихід з додатку...")
                        print("Дякуємо за використання.")
                        time.sleep(5)
                        exit()
                    else:
                        print("Помилка перезапустіть додаток...")
                        time.sleep(5)
                def register():
                    print("Введіть ваш вік:")
                    age=int(input())
                    if age<16:
                        print("Ой... Вибачте але SXServiseCLI 16+... Повертайтесь пізніше...")
                        print("Дякуємо за використання.")
                        time.sleep(5)
                        exit()
                    elif age>=16:
                        global user0_name
                        global user0_mail
                        global user0_password
                        print("Дякуємо. Перевірка віку пройдена.")
                        print("Далі проста регістрація.")
                        print("---> Введіть пошту")
                        user0_mail=input(">>> ")
                        print("---> Введіть імя користувача.")
                        user0_name=input(">>> ")
                        print("---> Придумайте пароль...")
                        user0_password=input(">>> ")
                        print("Дякуємо за інформацію!")
                        print(" ")
                        print(" - - - Картка користувача: - - - ")
                        print("╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╕")
                        print("╟ UserName - "+user0_name+"╢")
                        print("╟ UserMail - "+user0_mail+"╢")
                        print("╟ UserPassword - "+user0_password+"╢")
                        print("╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╛")
                        print("""
                              Етап 3.5! Перевірка інформації.
                              1 - перевірте правельність інформації
                              2 - Зайдіть на сайт https://sxservise.firebaseapp.com/ й зарегіструйтесь з цією поштою й таким самим паролем
                              Що це за сайт? - Це сайт сервісу який використовується для авторизації
                                - УВАГА! -> ПЕРЕВІРТЕ ЧИ ІНФОРМАЦІЯ ОДНАКОВА!!!
                                - УВАГА! -> ПЕРЕВІРТЕ ПРАВИЛЬНІСТЬ!!!
                            
                            Якщо данні не будуть сходитись у вас НЕ БУДУТЬ ПРАЦЮВАТИ ДЕЯКІ ФУНКЦІЇ.    
                            Після успішної регістрації введіть "y". 
                            Продовжити? y/n
                              """)
                        weq=input(">>> ")
                        if weq=="y":
                            q4()
                        elif weq=="n":
                            print("Дякуємо за використання.")
                            time.sleep(5)
                            exit()
                        else:
                            print("Помилка перезапустіть додаток...")
                            time.sleep(5)
                    else:
                        print("Помилка перезапустіть додаток...")
                    time.sleep(5)
                q3=input(">>> ")
                if q3=="y":
                    register()
                elif q3=="n":
                    print("Окей... Вихід з додатку...")
                    print("Дякуємо за використання.")
                    time.sleep(5)
                    exit()
                else:
                    print("Помилка перезапустіть додаток...")
                    time.sleep(5)
            user14=input(">>> ")
            if user14=="y":
                p3()
            elif user14=="n":
                print("Окей... Вихід з додатку...")
                print("Дякуємо за використання.")
                time.sleep(5)
                exit()
            else:
                print("Помилка перезапустіть додаток...")
                time.sleep(5)
        use13=input(">>> ")
        if use13=="y":
            p2()
        elif use13=="n":
            print("Окей... Вихід з додатку...")
            print("Дякуємо за використання.")
            time.sleep(5)
            exit()
        else:
            print("Помилка перезапустіть додаток...")
            time.sleep(5)
        exit()
    use12=input(">>> ")
    if use12=="y":
        p1()
    elif use12=="n":
        print("Окей... Вихід з додатку...")
        print("Дякуємо за використання.")
        time.sleep(5)
        exit()
    else:
        print("Помилка перезапустіть додаток...")
        time.sleep(5)
        exit()

def start():
    user_lang = int(input(">>> "))
    if user_lang==0:
        exit()
    elif user_lang==1:
        uk_version_st()
    elif user_lang==2:
        pass
    else:
        print("ERROR! Please restart app... ")
        time.sleep(5)
start()
