# Name:                     CubedNUmbers.py
# Author:                   Andre Lima
# Date Created:             February 22, 2023
# Date Last Modified:       February 26, 2023
#
# Purpose:

#Create empty dictionary to store numbers and their cubes
cubedNum = {}

#Fill cubedNum with numbers 1-10 as keys and their cubes as values
for n in range(1, 11):
    cubedNum[n] = n ** 3

#Print dictionary cubenNum
print(cubedNum)
