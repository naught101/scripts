#!/bin/bash

read -p "Username: " user
read -s -p "Password: " pass

export http_proxy=http://$user:${pass}@proxy.newcastle.edu.au:8080/
export ftp_proxy=http://$user:${pass}@proxy.newcastle.edu.au:8080/

