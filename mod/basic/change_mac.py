import os

from mod.system.system_config.mac_gen import mac_maker, mac_new

def atk():
    valid = False
    while not valid:
        print("generating new mac...")
        mac = mac_maker()
        print("[MAC] ", mac)
        chk = input("do you want to use this mac [Y/N] ")
        chk.lower()
        if chk == "y":
            valid = True
        else:
            pass

    os.system("ifconfig")
    iface = input("enter interface to change: ")
    print("setting ",mac," as new mac...")
    mac_new(iface, mac)
    os.system("clear")
    print("[MAC] ", mac)
    print("[IFACE] ", iface)