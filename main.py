import os

# Fetch all Wi-Fi names u used to connected with
def check_names():
    log = os.popen("netsh wlan show profile").read()

    # format that string and create an array with those names
    formatted_log = log.split("All User Profile     : ")

    # remove unwanted elements in list
    formatted_log.pop(0)
    formatted_log.pop(1)

    # make a file that keeps names
    with open("log.txt", "w") as file:
        for index in formatted_log:
            file.write(index.strip() + "\n")


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


start = input("Welcome! \n1 --> show profiles\n0 --> exit\n")

if start == "1":
    check_names()
    with open("log.txt", "r") as f:
        j = 0
        for i in f.readlines():
            print(f"{j} => " + i)
            j += 1
    print("For select all Wi-Fi type '*'")
    code = input("Select a wifi name for password: ")
    if code != "*":
        passwords = os.popen(f'netsh wlan show profile name={code} key=clear').read()
        print(passwords)
    else:
        show_passwords()
        print("I created 'passwords.txt' file that contains all passwords...")
elif start == "0":
    print("Shutting down..")
else:
    print("Invalid input. Please enter 1 or 0.")
