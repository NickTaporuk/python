#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'

BASH_SONAR_RUN_PATH = '/home'
PASSW = '01041987'
USER  = 'nkuropatkin'
HOST  = 'sonar.itftc.com'

import paramiko
ssh=paramiko.SSHClient()

# print ssh
'''
    Init ssh client
'''
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
'''
    Connect ssh to server
'''
ssh.connect(HOST,username=USER,password=PASSW)
'''
    Run crush server ;)
'''

ssh.exec_command("cd /var/www/nabludai ")

ssh.exec_command("git pull origin master")
channel = ssh.get_transport().open_session()
channel.get_pty()
channel.settimeout(5)
channel.exec_command('sudo -s')
channel.send(PASSW+'\n')
print channel.recv(1024)

stdin, stdout, stderr = ssh.exec_command("sudo -s")
stdin.write("01041987\n")
stdin.flush()

stdin, stdout, stderr = ssh.exec_command("whoami")
# stdin, stdout, stderr = ssh.exec_command("sudo /etc/init.d/sonar-runner")
# stdin, stdout, stderr = ssh.exec_command("cd /var/www/nabludai && git pull origin master && sudo /etc/init.d/sonar-runner")

error = stderr.read().splitlines()
out   = stdout.read().splitlines()
# inn   = stdin.read().splitlines()
print error,out

ssh.close()
# stdin, stdout, stderr = ssh.exec_command("sudo -S reboot")
# stdin.write("< пароль пользователя>\n")
# stdin.flush()