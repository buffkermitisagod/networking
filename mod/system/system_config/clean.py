import os


from mod.system.system_config.shell import execute_suppressed

def clean():
    file_name = "__pycache__"
    print("[!] removing pycache files...")
    file_prefix = "mod/"
    
    # for normal files
    files = []
    files.append(os.listdir(file_prefix))
    for c in files:
        for i in c:
            print("[!] removing __pycache__ from ("+file_prefix+i+")")
            command = " rm -r "+str(file_prefix+i)+"/"+file_name
            execute_suppressed(command)
    
    # for system files
    files = []
    files.append(os.listdir("mod/system/"))

    for c in files:
        for i in c:
            print("[!] removing __pycache__ from (mod/system/"+i+"/"+file_name+")")
            command = " rm -r mod/system/"+i+"/"+file_name
            execute_suppressed(command)

    