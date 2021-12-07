import os
import random
from scapy.all import RandMAC

from mod.system.system_config.shell import output_suppressed


    
def mac_maker():
    mac = RandMAC()
    return mac


def mac_new(inter, ma):
    command = str("ifconfig "+inter+" down")
    x = output_suppressed(command)
    command = str("macchanger -m "+ma+" "+inter)
    x = output_suppressed(command)
    command = str("ifconfig "+inter+" up")
    x = output_suppressed(command)