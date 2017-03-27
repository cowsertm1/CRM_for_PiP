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
    print("1. Print to screen")
    print("2. Search")
    print("3. Add contact")
    print("4. Delete contact")
    print("5. Save")
    print("6. Quit")
    print()

def printSearchMenu():
    print()
    print("0. First Name")
    print("1. Last Name")
    print("2. Phone Number")
    print("3. Email")
    print()

def printSearchCriteria(field):
    print()
    print("What string in the field " + field + " do you want to search for?")

def printInvalidOption(command):
    print()
    print("", command, " is not a valid option.  Please select again.")
