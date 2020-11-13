import os
import sys
import getpass
from subprocess import call

name = 'server'
port = 22
ServerAliveInterval = 10
HostName = ''
user = getpass.getuser()

if sys.argv[1] == 'add':
	name = 'server'
	port = 22
	ServerAliveInterval = 10
	hostname = ''
	user = getpass.getuser()
	if len(sys.argv) > 5:
		name = sys.argv[2]
		port = 22
		ServerAliveInterval = 10
		hostname = ''
		user = getpass.getuser()
		for i, arg in enumerate(sys.argv):
			if arg in ['-p', '--port']:
				port = sys.argv[i+1]
			elif arg in ['-n', '--name']:
				name = sys.argv[i+1]
			elif arg in ['-h', '--hostname']:
				hostname = sys.argv[i+1]
	else:
		name = input('Name on this server: ')
		if (port := input('Ssh port (default 22): ')) == '':
			port = 22
		hostname = input('Server address: ')
		ServerAliveInterval = 10
	os.system(f'bash {os.getcwd()}/ezssh_add.sh {name} {user} {port} {hostname} {ServerAliveInterval}')
	call(['ssh-copy-id', name])
	os.system(f'cd ~/.bin/ezssh/ && git pull origin master && cp ~/.ssh/config . && git add config && git commit -m "added new server" && git push origin master && rm config && cd -')
elif sys.argv[1] == 'list':
	os.system('python3 lssv/lssv')
elif sys.argv[1] == 'init':
	gitrepo = input('Git remote address: ')
	os.system(f'cd ~/.bin/ezssh/ && git init && git remote add origin {gitrepo} && git pull origin master')
elif sys.argv[1] == 'update':
	os.system(f'cd ~/.bin/ezssh/ && git pull origin master && cp ~/.ssh/config . && git add config && git commit -m "added new server" && git push origin master && rm config && cd -')
else:
	call(['ssh', sys.argv[1]])
