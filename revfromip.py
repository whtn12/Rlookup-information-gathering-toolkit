#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise
# This Script is Written By
__author__='whtn'

import requests
import re
import os
import getpass


def menu():
	""" menu for the rights """
	print "------------------------------------------------------"
	print "- _ __   _                  -Hello, " + getpass.getuser() + "!"
	print "-' )  ) //       /         "
	print "- /--' // __ __ /_  . . _  "
	print "-/  \_</_(_)(_)/ <_(_/_/_)_ - "
	print "-                     /    "
	print "-                    '     "
	print "-                           -by whtn "
	print "------------------------------------------------------"
	return;

####################          RevFrom single domain or ip ##############
def revfromip() :
	""" rev lookup service """
	get = raw_input("[*]Input target domain, ip ?\n>   ")
	to_send = "http://viewdns.info/reverseip/?host=" + get + "&t=1"
	r = requests.get(to_send)
	result = r.content
	return result;

####################            domains filter               ###########

def domainsfilter(result) :
	""" domains filter """
	res = re.findall(r'<td>([a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})+)</td>',result)
	domains = [el[0] for el in res]
	for x in domains:
		print(x)

def scan():
	os.system("uname -o")
	print "------------------------------------------------------"
	x = revfromip()
	domainsfilter(x)
	new = raw_input("------------------------------------------------------\n[*]Want another scan ? Y/N \n  > ")
	new =new.upper()
	if new == "Y":
		scan()
	elif new =="N":
		print "[*]Quitting ..."
		quit()
	else :
		print "[*]Please check your input and try again!!"
		scan()
menu()
scan()
