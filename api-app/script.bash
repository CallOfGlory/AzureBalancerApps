#!/bin/bash

apt-get update -y
apt-get install -y python3 python3-pip python3-venv git

cd /home/azureuser
git clone https://github.com/CallOfGlory/AzureBalancerApps.git

cd AzureBalancerApps/api-app

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cat > /etc/systemd/system/api.service <<EOF
[Unit]
Description=API Django App
After=network.target

[Service]
User=azureuser
Group=www-data
WorkingDirectory=/home/azureuser/AzureBalancerApps/api-app
Environment="PATH=/home/azureuser/AzureBalancerApps/api-app/venv/bin"
ExecStart=/home/azureuser/AzureBalancerApps/api-app/venv/bin/python manage.py runserver 0.0.0.0:8001
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable api.service
systemctl start api.service