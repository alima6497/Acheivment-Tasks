# Name:                     InputLegnthChecker.py
# Author:                   Andre Lima
# Date Created:             January 30, 2023
# Date Last Modified:       Febuary 6, 2023
#
# Purpose:
# Has the user enter a valid username that is 1-20 characters long, contains at least one
# uppercase letter, and one number 0-9

#welcome message giving requirement for the user's name
print("Hello! please choose a username. Your username must be between 2-20 characters long, include at least one upper case letter, and one number.\n")


while True:
    #prompt user for a name
    userName = input("Enter a username: ").strip()

    if len(userName) < 2:                                       #checks userName is longer than one letter
        print("Sorry, username must be longer than one letter. Please re-enter it.\n")
    elif len(userName) > 20:                                    #checks userName isn't longer than 20 letters
        print("Sorry, username cannot be more than 20 letters in length. Please re-enter it.\n")
    elif userName == userName.lower() or userName.isalpha():    #checks userName for capitalization and number 0-9
        print("Sorry, username must contain at least one upper case letter and one number 0-9. Please re-enter it.\n")
    else:                                                       #prints userName if requirements met; loops if not
        print("\nYour username is " + userName + ". Thank you!")
        
        break