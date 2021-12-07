import os

if os.geteuid()==0:
  pass
else:
  print("[!] user needs to be root!")
  print("[!] re-run as root!")
  quit()

try:
    f = open("/usr/local/bin/network","r")
    print("[!] network allready installed!")
    quit()
except FileNotFoundError:
    pass

print("installing stage[1/2]...")
apt = ["macchanger"]
for x in apt:
    command = "apt-get install "+x
    os.system(command)

print("installing stage[2/2]..")
apt = ["scapy"]
for x in apt:
    command = "pip3 install "+x
    os.system(command)


print("adding to bash commands...")
path = "/bin/bash"

dir_path = os.path.dirname(os.path.realpath(__file__))
x = '''
#!/bin/bash
cmd="python3 '''+dir_path+'''/network.py"
echo $cmd
$cmd
'''
f = open("/usr/local/bin/network","x+")
f.write(x)
f.close()
os.system("chmod +x /usr/local/bin/network")

print("done!")
print("run command: netowrk")
print("try it out now!")
