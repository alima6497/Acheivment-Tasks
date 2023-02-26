# Name:                     UnitConverter.py
# Author:                   Andre Lima
# Date Created:             February 22, 2023
# Date Last Modified:       February 26, 2023
#
# Purpose:
# To convert tempurature or speed units from imperial to metric and vice versa

# Function: converTemp
# Description: Converts celsius to faranheight and vice versa
# Parameters: 
#       temp: Temperature as a value
#       unit: Current unit of tempurature
# Return Value:
#       tempConvert: Converted temperature as a value
def convertTemp(temp, unit):
    if unit == "C":
        tempConvert = (temp * 1.8) + 32

    elif unit == "F":
        tempConvert = (temp - 32) * (5/9)

    return(tempConvert)

# Function: convertSpeed
# Description: Converts KPH to MPH and vice versa
# Parameters:
#       speed: Speed as a value
#       unit: Current unit of speed
# Return Value:
#       speedConvert: Converted speed as a value
def convertSpeed(speed, unit):
    if unit == "KPH":
        speedConvert = speed / 1.609

    elif unit == "MPH":
        speedConvert = speed * 1.609
    return(speedConvert)

#Ask user if they're tempurature or speed
conversionType = input("Would you like to convert [1]temperature, or [2]speed?: ").strip()

#Convert tempurature
if conversionType == "1":
    #Get tempurature as a value and current unit of temperature from user
    temperature = float(input("What is the tempurature value you'd like to convert? [#]: ").strip())
    tempUnit = input("What unit are you converting from? [C/F]: ").strip().upper()

    #Print converted value
    if tempUnit == "C":
        print("\n{0:.2f}°C is {1:.2f}°F.".format(temperature, convertTemp(temperature,tempUnit)))

    elif tempUnit == "F":
        print("\n{0:.2f}°F is {1:.2f}°C.".format(temperature, convertTemp(temperature,tempUnit)))

#Convert speed
elif conversionType == "2":
    #Get speed as a value and current unit of speed from user
    speed = float(input("What is the speed value you'd like to convert? [#]: ").strip())
    speedUnit = input("What unit are you converting from? [KPH/MPH]: ").strip().upper()

    #Print converted value
    if speedUnit == "KPH":
        print("\n{0:.2f} kph is {1:.2f} mph.".format(speed, convertSpeed(speed, speedUnit)))

    elif speedUnit == "MPH":
        print("\n{0:.2f} mph is {1:.2f} kph.".format(speed, convertSpeed(speed, speedUnit)))
