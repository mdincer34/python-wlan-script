import os


# Fetch all WiFi names u used to connected with
def check_names():

    log = os.popen("netsh wlan show profile").read()

    # format that string and create an array with those names
    formatted_log = log.split("All User Profile     : ")

    # remove unwanted elements in list
    formatted_log.pop(0)
    formatted_log.pop(1)

    # make a file that keeps names
    with open("log.txt", "w") as f:
        j = 0
        for i in formatted_log:
            f.write(f"{j} => " + i.strip() + "\n")
            j += 1
