#!/usr/bin/env python

import subprocess
import os.path
import pkgutil
import sys

def main():
    genWordlist()
    checkUserList()

def genWordlist():
    print "First we will generate wordlist..."
    minchars = raw_input('Enter minimum number of characters: ')
    maxchars = raw_input('Enter maximum number of characters: ')
    extracrunch = raw_input('Enter addtional rules like charset, patterns and suffixes/prefxes (e.g: abcde14 -t @@@14  [!] For more info please see: man crunch) : ')

    cmd = "crunch "+minchars+" "+maxchars+" "+extracrunch+" -o pass.txt"
    subprocess.call(cmd, shell=True)

def checkUserList():
    if os.path.isfile('users.txt'):
        startNmap()
    else:
        print "You need to create a list of users... users.txt one user per line"

def startNmap():
    hostname = raw_input('Enter host: ')
    port = raw_input('Enter port: ')
    reqmethod = raw_input('Enter request method e.g POST: ')
    reqpath = raw_input('Enter request path e.g /login: ')
    cmd = "nmap -p "+port+" --script http-brute --script-args 'http-brute.hostname="+hostname+",http-brute.method="+reqmethod+",http-brute.path="+reqpath+",userdb=users.txt,passdb=pass.txt' -n -v "+hostname
    subprocess.call(cmd, shell=True)

if __name__=='__main__':
    main()
