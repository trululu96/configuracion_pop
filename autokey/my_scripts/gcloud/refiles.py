import subprocess
import os
import time

user = subprocess.check_output("whoami", shell = True).decode("utf-8").replace("\n" , '')

with open("/home/" + user + "/.scripts/gcloud_instance", 'r') as f: 
        instance = f.readlines(0)[0]



out = subprocess.check_output("gcloud compute instances describe "+instance+" | grep 'status'", shell = True)

out = out.decode('utf-8').replace(' ', '').replace('\n','').split(':')[1]

if out != 'RUNNING':
    dialog.info_dialog("Warning", 'The instance is not running')
    exit()
    
     
else:
    retCode1 ,folder_receive = dialog.choose_directory(title=f'where do you want to receive the file/s that comes from {instance}')
    if retCode1 == 0:
        retCode2, income = dialog.input_dialog(title = 'Folder/file in the remote host', 
                message = 'if empty nothing will be done')
        
        if retCode2 == 0:
            if income == '': 
                exit()
            else: 
                command = 'gcloud compute scp --recurse ' + instance + ':~/' + income + ' ' + folder_receive
                
                command = command.split(' ') 
                
                send = subprocess.Popen(command, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT)
                
                
                stdout_ , _ = send.communicate()
                send.kill()
                stdout_ = stdout_.decode('utf-8')
                if stdout_ == '':
                    retCode, choice = dialog.list_menu(['yes','no'], 
                                    title= f'hooray it worked ', 
                                    message= f'Do you wish to see the files ? ',
                                    default= 'yes')
                    if retCode == 0 and choice == 'yes':
                        os.system('nautilus '+folder_receive)
                else:
                    dialog.info_dialog("Output",stdout_)
                
                
                