#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise
# This Script is Written By
__author__='whtn'

import requests
import re

def menu():
	""" menu for the rights """
	print "- _ __   _                 "
	print "-' )  ) //       /         "
	print "- /--' // __ __ /_  . . _  "
	print "-/  \_</_(_)(_)/ <_(_/_/_)_"
	print "-                     /    "
	print "-                    '    -by whtn "
	return;

####################          RevFrom single domain or ip ##############
def revfromip() :
	""" rev lookup service """
	get = raw_input("Your domain, ip ?\n>   ")
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

menu()
x = revfromip() 
domainsfilter(x)
