pip install undervolt

sudo undervolt --read


sudo undervolt --core -75 --cache -75

sudo touch /etc/systemd/system/undervolt.service

sudo vim /etc/systemd/system/undervolt.service 
[Unit]
Description=undervolt

[Service]
Type=oneshot
# If you have installed undervolt globally (via sudo pip install):
ExecStart=/usr/local/bin/undervolt -v --core -150 --cache -150 


systemctl start undervolt

sudo touch /etc/systemd/system/undervolt.timer
sudo vim /etc/systemd/system/undervolt.timer


[Unit]
Description=Apply undervolt settings

[Timer]
Unit=undervolt.service
# Wait 2 minutes after boot before first applying
OnBootSec=2min
# Run every 30 seconds
OnUnitActiveSec=30

[Install]
WantedBy=multi-user.target

systemctl enable undervolt.timer
systemctl start undervolt.timer
