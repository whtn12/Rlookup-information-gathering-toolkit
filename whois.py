#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise
# This Script is Written By
__author__='whtn'

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



def whois():
    target = raw_input("[*]Input target domain, ip ?\n>   ")
    result = os.system("whois "+ target)

menu()
whois()
def new_scan():
    x = raw_input("------------------------------------------------------\n[*]Want another scan ? Y/N \n  > ")
    x = x.upper()
    if x =="N" :
        print "[*]Quitting ..."
        quit()
    elif x == "Y":
        whois()
        new_scan()
    else :
        print "[*]Please check your input and try again!!"
        new_scan()
new_scan()
