# Name:                     GeometryCalculator.py
# Author:                   Andre Lima
# Date Created:             January 30, 2023
# Date Last Modified:       Febuary 2, 2023
#
# Purpose:
# The program will find the area (in cm^2) and permimeter (in cm) of a 
# user selected shape given the radius (in cm) or legnth (in cm) of one
# of the sides

import math

'''
1. Welcome user
2. Provide options for different shape types
3. Get the length/radius from the user
4. Find the area and permimeter of the shape 
5. print the results
'''

# Function: circle
# Description: will output the area of a cirlce
# Parameters:
#   radius: radius of the circle
def circle(radius):
    area = math.pi * (radius ** 2)

    print("\nThe area of the circle is " + str(area) + "cm^2")

# Function: rectangle
# Description: will output the area and perimeter of a rectangle
# Parameters:
#   length: length of one of the sides of the rectangle
def rectangle(length):
    area = length ** 2
    perimeter = length * 4

    print("\nThe area of the rectangle is " + str(area) + "cm^2\n" +
    "The perimeter of the rectangle is " + str(perimeter) + "cm")

# Function: triangle
# Description: will output the area and perimeter of a triangle
# Parameters:
#   length: length of one of the sides of the triangle
def triangle(length):
    area = (math.sqrt(3) / 4) * length ** 2
    perimeter = length * 3

    print("\nThe area of the triangle is " + str(area) + "cm^2\n" +
    "The perimeter of the triangle is " + str(perimeter) + "cm")

#print shape selction dialog
print("Geometry Calculater\n\n" +
    "1. Calculate the Area of a Circle\n" +
    "2. Calculate the Area of a Rectangle\n" +
    "3. Calculate the Area of a Triangle\n" +
    "4. Quit\n")

shapeSelection = int(input("Enter your choice (1-4): "))

if shapeSelection == 1:     #find the area of a cirlce and print result
    #prompt user for radius of circle and send to function circle
    circle(float(input("\nEnter the radius of the circle (in cm): ")))
elif shapeSelection == 2:   #find the area and permimeter of a square and print results
    #prompt user for length of rectangle and send to function rectangle
    rectangle(float(input("\nEnter the legnth of the rectangle (in cm): ")))
elif shapeSelection == 3:   #find the area and premimeter of a triangle and print results
    #prompt user for length of triangle and send to function triangle
    triangle(float(input("\nEnter the legnth of the triangle (in cm): ")))
elif shapeSelection == 4:   #goodbye message if the user quits
    print("\nThank you for using Geometery Calculator. Goodbye!")
else:                       #goodbye message if no valid input given
    print("\nSorry, not a valid input. Goodbye!")