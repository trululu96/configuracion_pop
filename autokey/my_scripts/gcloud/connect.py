import subprocess
import os
import time

user = subprocess.check_output("whoami", shell = True).decode("utf-8").replace("\n" , '')

with open("/home/" + user + "/.scripts/gcloud_instance", 'r') as f: 
        instance = f.readlines(0)[0]



out = subprocess.check_output("gcloud compute instances describe "+instance+" | grep 'status'", shell = True)

out = out.decode('utf-8').replace(' ', '').replace('\n','').split(':')[1]

if out == 'TERMINATED':
    retCode, choice = dialog.list_menu(['yes','no'], 
                                        title= f'{instance} not started', 
                                        message= f'Do you wish to start {instance} ? \n it might take a while')

    if retCode == 0: 
        if choice == 'yes': 
            start = subprocess.Popen(['gcloud', 'compute', 'instances','start', instance], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.STDOUT)

            stdout, _ = start.communicate()
            
            start.kill()
            
            if 'done' not in stdout.decode('utf-8').split('\n')[1]:
                dialog.info_dialog("Something went wrong", stdout.decode('utf-8'))
            else:
                time.sleep(15)
                os.system(f"gnome-terminal -- /bin/sh -c 'gcloud compute ssh {instance} ; exec bash' ")

                    
else:
    os.system(f"gnome-terminal -- /bin/sh -c 'gcloud compute ssh {instance} ; exec bash' ")







