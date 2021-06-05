# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 08:34:59 2021

@author: maxperezt

"""
from os import remove
from shutil import copyfile

WEBSITE_BLOCK_FILENAME = "websitesBlocked.txt"
HOST_FILENAME = r"C:\Windows\System32\drivers\etc\hosts"
COPY_HOST_FILENAME = "hosts"
localHostIp = "127.0.0.1"

def loadWebsites():
    """
    Returns a LIST of the websites to be blocked
    """
    inFile = open(WEBSITE_BLOCK_FILENAME, 'r')
    #Every line of text in the file is a website
    websitesBlockedList = inFile.read().splitlines()
    inFile.close()
    return websitesBlockedList

def blockWebsites(websitesList):
    """
    websitesList : List, the websites that are going to be blocked
    
    It mapps the local host ip to the website name in the Windows Host file, so the browser never finds the server
    """
    inFile = open(HOST_FILENAME,'a')
    inFile.write("\n")
    
    print("The following websites have been blocked: ")
    for website in websitesList:
        inFile.write(localHostIp + ' ' + website)
        print(website)
    
    inFile.close()
    
def unblockWebsites():
    """
    Restablish the original hosts file unblocking the websites
    """
    copyfile(COPY_HOST_FILENAME, HOST_FILENAME)
    
#we make a copy of the original hosts file, so we can restablish when we don't want the sites to be blocked any longer
copyfile(HOST_FILENAME, COPY_HOST_FILENAME)

websitesList = loadWebsites()
blockWebsites(websitesList)

checkUnblock = input("\nEnter unblock to access the websites listed again: ")
if checkUnblock.lower() == "unblock":
    unblockWebsites()
    