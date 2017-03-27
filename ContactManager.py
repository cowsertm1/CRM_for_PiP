################################################################################
# File Name:	ContactManager.py
# Author:		Matt Cowsert with skeleton support from Debbie Heisler via Github
# Date:			March 27, 2017
# Description:
#   This is the contact manager's main driver function/file.
################################################################################

import Person
import List
import Menus
import os

fname = "contacts.dat"
try:
    file = open(fname, 'r')
except IOError:
    file = open(fname, 'w')

quit = False  # global variable to exiting the application easier
contactList = List.List()

def readInContacts():
    # Read in the default contact list file
    file = open(fname, 'r')
    for line in file:
        fields = line.split(',')
        peep = Person.Person(fields[0].strip(), fields[1].strip(), fields[2].strip(), fields[3].strip())
        contactList.addPerson(peep)


def printContactsToFile():
    # Print the contacts to a file.  Will loop until the application finds a good file name
    while True:
        print("File Name")
        fn = input()
        try:
            file = open(fn, 'w')
            contactList.printToFile(file)
            print("Contacts saved to " + fn)
            break
        except IOError:
            continue


def addNewContact():
    # Adds a new contact to the contact manager. Does not check for errors
    global contactList
    print("First Name:", )
    fn = input()
    print("Last Name:", )
    ln = input()
    print("Phone Number:", )
    pn = input()
    print("Email:", )
    email = input()
    peep = Person.Person(fn, ln, pn, email)
    contactList.addPerson(peep)

def handleFoundPerson(person, option):
    # Error checks person.  Prints it or an error
    if person is None:
        print("No one matches that criteria")
    elif option == "search":
        person.printToScreen()
    elif option == "delete":
        contactList.deletePerson(person)
        print("Contact has been deleted")

def checkSearchInput(selected, option):
    # Handles the input for searching.
    if selected == "f":
        Menus.printSearchCriteria("First Name")
        searchStr = input()
        peep = contactList.matchPersonByFirstName(searchStr)
        handleFoundPerson(peep, option)
    elif selected == "l":
        Menus.printSearchCriteria("Last Name")
        searchStr = input()
        peep = contactList.matchPersonByLastName(searchStr)
        handleFoundPerson(peep, option)
    elif selected == "pn":
        Menus.printSearchCriteria("Phone Number")
        searchStr = input()
        peep = contactList.matchPersonByPhoneNumber(searchStr)
        handleFoundPerson(peep, option)
    elif selected == "e":
        Menus.printSearchCriteria("Email")
        searchStr = input()
        peep = contactList.matchPersonByEmail(searchStr)
        handleFoundPerson(peep, option)
    else:
        print("That is not a valid selection")

def searchForPerson(option):
    # Handles the option to search for a person to print or delete
    Menus.printSearchMenu()
    while True:
        try:
            selection = int(input())
            checkSearchInput(selection, option)
            break
        except ValueError:
            print("Numbers only.  Try again")
            continue

def checkInput(selected):
    # Checks the input to make sure it is a valid main menu option
    global quit
    if selected == "pr":
        contactList.printToScreen()
    elif selected == "s":
        searchForPerson("search")
    elif selected == "a":
        addNewContact()
    elif selected == "d":
        searchForPerson("delete")
    elif selected == "sv":
        printContactsToFile()
    elif selected == "h":
        print("Please direct all questions to Matt Cowsert @ mtc434@stern.nyu.edu")
    elif selected == "q":
        quit = True
    else:
        Menus.printInvalidOption(selected)

# The Main function

if __name__ == "__main__":
    readInContacts()

    while (quit == False):
        Menus.printMainMenu()
        try:
            selection = str(input())
            checkInput(selection)
        except ValueError:
            continue
