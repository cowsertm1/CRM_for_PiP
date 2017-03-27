################################################################################
# File Name:	Menus.py
# Author:		Matt Cowsert with skeleton support from Debbie Heisler via Github
# Date:			March 27, 2017
# Description:
#	This file contains all the menus needed for the contact manager. 
#	Each function will print out a menu.
################################################################################

def printMainMenu():
    print()
    print("pr. Print Contacts")
    print("s. Search Contacts")
    print("a. Add Contact")
    print("d. Delete Contact")
    print("sv. Save Changes")
    print("h. Help")
    print("q. Quit Application")
    print()

def printSearchMenu():
    print()
    print("fn. First Name")
    print("ln. Last Name")
    print("pn. Phone Number")
    print("e. Email")
    print()

def printSearchCriteria(field):
    print()
    print("What " + field + " do you want to search for?")

def printInvalidOption(command):
    print()
    print("",command,  "is not a valid option.  Please select again.")
