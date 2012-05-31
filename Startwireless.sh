#!/bin/bash

insmod /lib/modules/`uname -r`/kernel/drivers/usb/serial/usbserial.ko vendor=0x16d8 product=0x6280
iptables -t nat -A POSTROUTING -o ppp0 -j MASQUERADE
ifconfig eth0 192.168.2.100
/etc/init.d/dhcp3-server restart