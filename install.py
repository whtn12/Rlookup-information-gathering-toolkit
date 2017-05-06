#!/usr/bin/python
import os
''' Installing requirements '''
print "[*]Requirements needed to run this tool : \n [*]------------------------------------------------[*]\n"
list = open("requirements.txt").readlines()
for x in list:
    x.replace("n", "")
    print "                [*]" + x

answer = raw_input(" [*]Whannah install that ? Y/N \n [*]------------------------------------------------[*]\n> ")
answer = answer.upper()
if answer == "Y":
    print "[*] Installing ..."
    os.system("pip install -r requirements.txt")
    print "Done "
elif answer == "N":
    print "[*]quitting ..."
    quit()
else :
    print "[*]Please check your input and try again..."
    os.system("python install.py")
