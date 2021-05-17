#!/usr/bin/python3

import subprocess
import re


playbook=subprocess.run(['ansible-playbook', '-i', 'localhost', 'playbook.yml'],capture_output=True, text=True).stdout
ipaddres=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',playbook)
ipaddr="\n".join(ipaddres)

writefile=f'[workstation]\n{ipaddr}\n'
with open('host', 'w') as file: 
    file.write(writefile)
