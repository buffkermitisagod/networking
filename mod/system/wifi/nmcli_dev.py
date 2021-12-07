import subprocess

def get_wifi(iface):
    command = "nmcli dev wifi"
    res = subprocess.run(command, shell=True, capture_output=True, text=True)
    wifi = res.stdout
    wifi = wifi.split("\n")
    return wifi

def conect(iface, pas, ssid):
    command = 'nmcli d wifi connect "'+ssid+'" password '+pas+' ifname '+iface
    res = subprocess.run(command, shell=True, capture_output=True, text=True)
    suc_chk = res.stdout
    if "successfull" in suc_chk:
        return True
    else:
        return False