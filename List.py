###############################################################################
# File Name:	List.py
# Author:		Matt Cowsert with skeleton support from Debbie Heisler via Github
# Date:			March 27, 2017
# Description:
#	This class represents a list.  It is a list of Person.  You can add to
#	the list.  You can take from the list.  You can match an entity in the list
#	based on the members of the Person.  It can also print itself out to
#	the screen and to a file
###############################################################################

class List:
    # List class contains methods and members to describe one list
    def __init__(self):
        # Initializes the empty list
        self.innerList = []

    def addPerson(self, person):
        # Adds this person to the list
        self.innerList.append(person)

    def printToScreen(self):
        # Prints each person to the screen
        # print self.innerList
        for peep in self.innerList:
            peep.printToScreen()

    def printToFile(self, fn):
        # Saves each person to the given file
        for peep in self.innerList:
            peep.printToFile(fn)

    def matchPersonByFirstName(self, fn):
        # Finds the first person from the list matching the given string
        # based on the first name. Returns that person or None if not found
        for peep in self.innerList:
            if (peep.inFirstName(fn)):
                return peep
        return None

    def matchPersonByLastName(self, ln):
        # Finds the first person from the list matching the given string
        # based on the last name.  Returns that person or None if not found
        for peep in self.innerList:
            if (peep.inLastName(ln)):
                return peep
        return None

    def matchPersonByPhoneNumber(self, pn):
        # Finds the first person from the list matching the given numbers
        # based on the phone number.  Returns that person or None if not found
        for peep in self.innerList:
            if (peep.inPhoneNumber(pn)):
                return peep
        return None

    def matchPersonByEmail(self, em):
        # Finds the first person from the list matching the given string
        # based on the email address.  Returns that person or None if not found
        for peep in self.innerList:
            if (peep.inEmail(em)):
                return peep
        return None

    def deletePerson(self, peep):
        # Deletes the given person.
        # Returns -1 if there is no one to delete.
        # Returns 0 if it was able to delete someone. """
            if peep is None:
                return -1
            else:
                self.innerList.remove(peep)
            return 0


