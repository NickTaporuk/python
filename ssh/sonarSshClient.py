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
#
# ssh.exec_command("cd /var/nabludai | ")
#
# ssh.exec_command("git pull origin master")
#
# stdin, stdout, stderr = ssh.exec_command("sudo /etc/init.d/sonar-runner")
stdin, stdout, stderr = ssh.exec_command("cd /var/www/nabludai && git pull origin master && bash sudo /etc/init.d/sonar-runner")
# stdin.write("01041987\n")
# stdin.flush()
error = stderr.read().splitlines()
out   = stdout.read().splitlines()
# inn   = stdin.read().splitlines()
print error,out
# stdin, stdout, stderr = ssh.exec_command("sudo -S reboot")
# stdin.write("< пароль пользователя>\n")
# stdin.flush()