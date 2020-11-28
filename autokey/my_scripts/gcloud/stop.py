import subprocess

start = subprocess.Popen(['gcloud', 'compute', 'instances','list'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)

stdout, _ = start.communicate() 


instances = stdout.decode('utf-8').split('\n')[0:-1]
start.kill() 

active_instances = []
for i in [' '.join(i.split()).split(' ') for i in instances]:
    if i[-1]=='RUNNING':
        active_instances.append(i[0])

if len(active_instances) == 0: 
    status,message = 0, 'there are no active instances'
else: 
    status, message = 1, 'you wanna kill this instances: ' + ' '.join(active_instances) + ' ?'

if status == 0: 
    dialog.info_dialog('no active instances', message)

else: 
    retCode, choice = dialog.list_menu(['yes','kill less instances'], title= 'u sure?',
                            message = message)
       
    if retCode == 0: 
        if choice != 'yes':
            retCode, choice = dialog.list_menu_multi(active_instances, title = 'which ones you wanna kill?')
            if retCode != 0: 
                exit()
            active_instances = choice
            
        start = subprocess.Popen(['gcloud', 'compute', 'instances','stop'] + active_instances, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)
        stdout, _ = start.communicate()
        start.kill()
        dialog.info_dialog("Output", stdout.decode('utf-8'))    

 
        