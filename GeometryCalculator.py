# Name:                     GeometryCalculator.py
# Author:                   Andre Lima
# Date Created:             January 30, 2023
# Date Last Modified:       January 30, 2023
#
# Purpose:
# The program will find the area (in cm^2) and permimeter (in cm) of a 
# user selected shape given the radius (in cm) or legnth (in cm) of one
# of the sides

import math

#print shape selction dialog
print("Geometry Calculater\n\n" +
    "1. Calculate the Area of a Circle\n" +
    "2. Calculate the Area of a Rectangle\n" +
    "3. Calculate the Area of a Triangle\n" +
    "4. Quit\n")

shapeSelection = int(input("Enter your choice (1-4): "))

if shapeSelection == 1:     #find the area of a cirlce and print result
    #prompt user for radius of circle
    circleRadius = float(input("\nEnter the radius of the circle (in cm): "))
    circleArea = math.pi * (circleRadius ** 2)

    print("\nThe area of the circle is " + str(circleArea) + "cm^2")
elif shapeSelection == 2:   #find the area and permimeter of a square and print results
    #prompt user for length of rectanlge
    rectangleLength = float(input("\nEnter the legnth of the rectangle (in cm): "))
    rectangleArea = rectangleLength ** 2
    rectanglePermimeter = rectangleLength * 4

    print("\nThe area of the rectangle is " + str(rectangleArea) + "cm^2\n" +
    "The perimeter of the rectangle is " + str(rectanglePermimeter) + "cm")
elif shapeSelection == 3:   #find the area and premimeter of a triangle and print results
    #prompt user for length of triangle
    triangleLength = float(input("\nEnter the legnth of the triangle (in cm): "))
    triangleArea = (math.sqrt(3) / 4) * triangleLength ** 2
    trianglePermimeter = triangleLength * 3

    print("\nThe area of the triangle is " + str(triangleArea) + "cm^2\n" +
    "The perimeter of the rectangle is " + str(trianglePermimeter) + "cm")
elif shapeSelection == 4:   #goodbye message if the user quits
    print("\nThank you for using Geometery Calculator. Goodbye!")
else:                       #goodbye message if no valid input given
    print("\nSorry, not a valid input. Goodbye!")