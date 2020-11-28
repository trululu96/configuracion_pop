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
    retCode1 ,file_to_send = dialog.choose_directory(title=f'File to send to {instance}')
    if retCode1 == 0:
        retCode2, folder_r = dialog.input_dialog(title = 'Folder in the remote host', message = 'if empty then it will be send to ~/')
        
        if retCode2 != 0:
            folder_r = '~'
        else:
            folder_r = '~/' + folder_r
        
        command = 'gcloud compute scp ' + file_to_send + ' ' + instance + ':' +folder_r  
        
        command = command.split(' ') 
                
        send = subprocess.Popen(command, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT)
                
                
        stdout_ , _ = send.communicate()
        send.kill()
        stdout_ = stdout_.decode('utf-8') 
        stdout_ = 'success' if stdout_ == '' else stdout_
        dialog.info_dialog("Output",stdout_)