# Name:                     CourseRegistration.py
# Author:                   Andre Lima
# Date Created:             February 23, 2023
# Date Last Modified:       February 26, 2023
#
# Purpose: To let students register for courses

#Get student infromation
studentInfo = {
    "firstName": input("Please input your first name: ").capitalize(),
    "lastName": input("Please input your lst name: ").capitalize(),
    "studentNumber": input("Please input your student number: ")
}
courses = {
    "PROG1783": "Support Programming Fundamentals",
    "INFO1385": "Network Infrastructure I",
    "INFO1250": "Computer Systems Fudamentals",
    "COMM1085": "College Reading & Writing Skills"
}

#List courses available for registration
print("\nCourses available for registration: \n{0:-^41}".format("-"))
for n in courses:
    print(n, courses[n])
print("{0:-^41}".format("-"))

#Prompt student for what courses they want to register
registration = (input("Please enter the course codes for courses you want to register for, seperated by commas [CC,CC]:\n").upper()).split(",")

#Print student information and courses they registered for
print("\nCourse Registration for {} {} {}:".format(studentInfo["firstName"], studentInfo["lastName"], studentInfo["studentNumber"]))
for n in registration:
    print(n, courses[n])