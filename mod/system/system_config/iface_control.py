import os

def put_into_monitor(iface):
    command = "airmon-ng start "+iface
    os.system(command)
    iface = iface+"mon"
    return iface

def put_into_managed(iface):
    command = "airmon-ng stop "+iface
    os.system(command)