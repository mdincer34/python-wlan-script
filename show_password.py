import os


def show_passwords():
    with open("log.txt", "r") as f:
        log = [i.strip() for i in f.readlines()]

    for i in log:
        names = []
        pass_log = os.popen(f'netsh wlan show profile name="{i}" key=clear').read()
        log_list = pass_log.split("\n")
        with open("passwords.txt", "a") as f:
            for j in log_list:
                if "    Name                   : " in j:
                    names.append("name : " + j.split("    Name                   : ")[1].strip())
                elif "    Key Content            : " in j:
                    names.append("password: " + j.split("    Key Content            : ")[1].strip())
            if names:
                print(names)
                f.writelines([name + "\n" for name in names])