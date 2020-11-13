#!/bin/bash

cat <<EOT >> ~/.ssh/config
Host $1
	User $2
	Port $3
	HostName $4
	ServerAliveInterval $5

EOT