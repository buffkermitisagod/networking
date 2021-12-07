from scapy.all import *

from mod.system.system_config.get_ip import get_default_gateway_linux as gate

def atk(r=False):
    ip = gate()
    rang = ip+"/24"
    print("[GATEWAY] "+ip)
    print("[RANGE] "+rang)
    print("scanning...")
    if not r:

        target_ip = rang
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp

        result = srp(packet, timeout=3, verbose=0)[0]
        clients = []

        for sent, received in result:
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        print("\n\n=====================================")
        print("available devices in the network:")
        print("")
        print("IP" + " "*18+"MAC")
        for client in clients:
            print("{:16}    {}".format(client['ip'], client['mac']))
        print("\n=====================================")
    if r:
        target_ip = rang
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp

        result = srp(packet, timeout=3, verbose=0)[0]
        clients = []

        for sent, received in result:
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        return clients
    else:
        pass
