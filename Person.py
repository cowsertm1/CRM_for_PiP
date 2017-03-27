################################################################################
# File name:	Person.py
# Author:		Matt Cowsert with skeleton support from Debbie Heisler via Github
# Date:			March 27, 2017
# Description:
#	This class represents an individual contact. It contains their first name,
#	last name, and email address.  It can print out itself
################################################################################

class Person:

    def __init__(self, fn, ln, pn, em):
        # Initialize a person with the give first name, last name, phone number and email address
        self.firstName = fn
        self.lastName = ln
        self.phoneNumber = pn
        self.email = em

    def printToScreen(self):
        """ Prints the person information to the screen """
        formatted = "\t" + self.firstName + "\t\t" + self.lastName + "\t\t" + self.phoneNumber + "\t\t" + self.email
        print(formatted)

    def copyToFile(self, fn):
        """ Prints the person information to the given file, fn """
        formatted = self.firstName + "," + self.lastName + "," + self.phoneNumber + "," + self.email + "\n"
        fn.write(formatted)

    def inFirstName(self, match):
    # Returns true if match is contained in the first name. False otherwise.  Case insensitive """
        if (self.firstName.lower().find(match.lower()) < 0):
            return False
        else:
            return True
    	
    def inLastName(self, match):
    	""" Returns true if match is contained in the last name.
    	False otherwise. Case insensitive """
    	if (self.lastName.lower().find(match.lower()) < 0):
    		return False
    	else:
    		return True

    def inPhoneNumber(self, match):
    	""" Returns true if match is contained in the Phone Number.
    	False otherwise.  Case insensitive """
    	if (self.phoneNumber.lower().find(match.lower()) < 0):
    		return False
    	else:
    		return True

    def inEmail(self, match):
    	""" Returns true if match is contained in the email address.
    	False otherwise.  Case insensitive """
    	if (self.email.lower().find(match.lower()) < 0):
    		return False
    	else:
    		return True
