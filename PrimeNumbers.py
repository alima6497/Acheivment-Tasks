# Name:                     PrimeNumbers.py
# Author:                   Andre Lima
# Date Created:             February 22, 2023
# Date Last Modified:       JFebruary 26, 2023
#
# Purpose:

# Function: isPrime
# Description: determine if a number is prime or not
# Parameters:
#       number: a whole number
# Return Value:
#       boolean: True if prime, False if composite
def isPrime(number):
    if number <= 1:
        return False

    for n in range(2, number):
       if number % n == 0:
            return False

    return True

#Welcome message
print("Welcome! This program will sort through a list of integers and devide them into prime and non-prime numbers.")

#Prompt user for a list of whole numbers, csat them as int, and sort the list
numbers = sorted(map(int, input("Please enter a set of whole numbers seperated by commas[#,#]: ").split(",")))
#Create empty lists to store prime and composite numbers
numbersPrime = []
numbersComposite = []

#Check each number in list numbers, checks if prime, and adds them to respective list
for n in numbers:
    if isPrime(n):
        numbersPrime.append(n)
    else:
        numbersComposite.append(n)

#Print prime numbers in list
if numbersPrime:
    print("Prime numbers are", ",".join(map(str, numbersPrime)))
else:
    print("There are no prime numbers in the list.")

#Print composite numbers in list
if numbersComposite:
    print("Non-prime numbers are", ",".join(map(str, numbersComposite)))
else:
    print("There are no non-prime numbers in the list.")
