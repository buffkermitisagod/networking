import os
import importlib

from mod.system.system_config.clean import clean

if os.geteuid()==0:
  pass
else:
  print("[!] user needs to be root!")
  print("[!] re-run as root!")
  quit()

def use(mod):
    try:
        my_module = importlib.import_module(mod)
        return my_module, True
    except ModuleNotFoundError:
        print("[!] module ("+mod+") not found!")
        return None, False

def list(t):
    if t == "None":
        files = []
        dirs = os.listdir("mod")
        dirs.remove("system")
        for d in dirs:
            if d == "system":
                pass
            else:
                files.append(os.listdir(str("mod/"+d)))
        
        c = 0
        for c in range(len(files)):
            i = files[c]
            d = dirs[c] 
            print("\n\n============["+dirs[c]+"]============")
            for x in i:
                if x == "__pycache__":
                    pass
                else:
                    print("mod/"+d+"/"+x)
            print("================================\n\n")

    else:
        try:
            files = os.listdir(str("mod/"+t))
            print("\n\n============["+t+"]============")
            for i in files:
                if i == "__pycache__":
                    pass
                else:
                    print("mod/"+t+"/"+i)
            print("================================\n\n")
        except FileNotFoundError:
            print("[!] module file ("+t+") not found!")
            

os.system("clear")

help = """
use *module* ->  select module to use
run          ->   run the selected attack
list *type*  ->  list attacks (the type of attack is optional)
clear        ->   clear the screen 

"""


banner = """

            _                      _    _             
 _ __   ___| |___      _____  _ __| | _(_)_ __   __ _ 
| '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / | '_ \ / _` |
| | | |  __/ |_ \ V  V / (_) | |  |   <| | | | | (_| |
|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\_|_| |_|\__, |
=================================================|___/ 
                Networking In Python
=================================================
[?] use 'help' for list of commands

"""

print(banner)

mod = ""

try:
    while True:
        cho = input("~/Networking/"+mod+"$ ")
        if cho == "help":
            print(help)
        elif cho == "clear":
            os.system("clear")
            print(banner)


        elif "list" in cho:
            cho = cho.split(" ")
            try:
                l = cho[1]
            except IndexError:
                l = "None"
            list(l)


        elif "use" in cho:
            cho = cho.split(" ")
            try:
                mod = cho[1]
                mo = mod.replace("/",".")
                mo = mo.replace(".py","")
                m = True
            except IndexError:
                print("[!] no module selected!")
                m = False
            if m:
                run, sel = use(mo)
            else:
                pass
        elif cho == "run":
            if sel:
                run.atk()
            else:
                print("[!] no module selected!")
        
        elif cho == "" or " " or "\n":
            print("\n\n")
        else:
            print("[!] not renonised command!")
except KeyboardInterrupt:
    print("[!] user exit, cleaning __pychache__ files")
    clean()