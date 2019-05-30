#! python3
# PasswordDetection.py - This is a programm which we can use to Detect if our Password is strong or not.
# Strong password have : 1digit, 8characters long, uppercase and lowercase
import re, sys

lengthRegex = re.compile(r'([\w]{8,})', re.VERBOSE)

digitRegex = re.compile(r'([\d] )', re.VERBOSE)
upperRegex = re.compile(r'([A-Z] )', re.VERBOSE)
lowerRegex = re.compile(r'([a-z] )', re.VERBOSE)

password=input("Give me YoursPassword, at least 8symbols, 1 uppercase, 1 lowercase and 1 digit : ",)

try:
    mo = lengthRegex.search(password).group()               #Checking for minimum of 8characters long
    print("Yours password is correct for long ")
except:
    print("Password is to short")
    sys.exit()
try:
    mo = digitRegex.search(password).group()               #Checking for minimum 1digit
    print("Yours password is correct for digit ")
except:
    print("Password need a digit")
    sys.exit()

try:
    mo = upperRegex.search(password).group()               #Checking for Uppercase
    print("Yours password is correct for Uppercase ")
except:
    print("Password need a Uppercase")
    sys.exit()

try:
    mo = lowerRegex.search(password).group()               #Checking for Lowercase
    print("Yours password is correct for Lowercase ")
except:
    print("Password need a Lowercase")
    sys.exit()
