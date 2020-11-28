# Enter script 

import subprocess

out = subprocess.check_output("gcloud compute instances list | awk '{print $1}' | tail -n +2", shell = True)
user = subprocess.check_output(["whoami"]).decode("utf-8").replace("\n" , '')


out = [i for i in out.decode("utf-8").split('\n') if i != '']

retCode, choice = dialog.list_menu(out)
if retCode == 0:
    with open("/home/" + user + "/.scripts/gcloud_instance", 'w') as f: 
        f.writelines(choice)  
    