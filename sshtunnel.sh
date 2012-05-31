#!/bin/bash

ssh -f naught101@$1 -L 10000:$1:10000 -N

#The -f tells ssh to go into the background just before it executes the command. 
#This is followed by the username and server you are logging into. 
#The -L 2000:personal-server.com:25  is in the form of -L local-port:host:remote-port. 
#Finally the -N instructs OpenSSH to not execute a command on the remote system
