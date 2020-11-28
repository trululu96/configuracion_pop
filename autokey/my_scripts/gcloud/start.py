# Enter script code
import subprocess
user = subprocess.check_output("whoami", shell = True).decode("utf-8").replace("\n" , '')
with open("/home/" + user + "/.scripts/gcloud_instance", 'r') as f: 
        instance = f.readlines(0)[0]


out = subprocess.Popen(['gcloud', 'compute', 'instances','start', instance], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)

stdout, _ = out.communicate()
out.kill()
dialog.info_dialog("Output", stdout)