"""
Credit Card Validator
Created by Braden Piper, bradenpiper.com
Created on Thu Jan 16, 2023
Version = 1.0
------------------------------------------
DESCRIPTION:
A program that checks the validity of a credit card number using Luhn's Algorithm.
The program accepts an input of a credit card number, and will calculate if the
number is syntactically valid using Luhn's Algorithm. In addition to checking the
validity of the card number, the program will also identify if the credit card number
is one issued by American Express, Visa, or Mastercard.
------------------------------------------
NOTES:
• This program is meant for educational purposes only, and is not meant to be used
as an actual tool for validating credit card numbers.
• This program will only work for credit card numbers of American Express, Visa, and
Mastercard. Credit card numbers issued from other companies will be considered invalid.
• This program will only work with credit card numbers of length 13, 15, or 16 digits.
• This program will only work with Mastercard numbers starting in numbers 51, 52,
53, 54, or 55.
"""


# FUNCTION DEFINITIONS

def getLength(num):
    '''
    accepts an integer, returns the number of digits in that integer
    '''
    stringnum = str(num)
    length = len(stringnum)
    return length

def getLastDigit(num):
    '''
    accepts an integer, returns the last digit of that integer
    '''
    return (num % 10)

def shorten(num):
    '''
    accepts an integer, returns the same integer with the last digit removed
    '''
    return int(num / 10)

def getFirstDigit(num):
    '''
    accepts an integer, returns the first digit of that integer
    '''
    numLength = getLength(num)
    for x in range(numLength-1):
        num = shorten(num)
    return num

def getFirst2Digits(num):
    '''
    accepts an integer, returns the first two digits of that integer
    '''
    numLength = getLength(num)
    for x in range(numLength-2):
        num = shorten(num)
    return num

def calculateChecksum(ccnum):
    '''
    accepts a credit card number, returns the checksum of the cc number
    '''
    sum = 0
    for x in range(cclength):
        sum += getLastDigit(ccnum)             # add last digit to sum
        ccnum = shorten(ccnum)                # shorten ccnumb by 1
        nextnum = (getLastDigit(ccnum)) * 2    # get last digit, multiply by 2
        lastdigitlength = getLength(nextnum)    # get length of lastdigit
        if lastdigitlength == 1:                # if one digit, add to sum
            sum += nextnum
        else:                                   # otherwise
            sum += getLastDigit(nextnum)        # get the last digit of nextnum, add it to sum
            nextnumshorter = shorten(nextnum)   # shorten by 1
            sum += getLastDigit(nextnumshorter) # get last digit, add it to sum
        ccnum = shorten(ccnum) # shorten ccnumb by 1
    return sum

# PROGRAM

# Get Credit Card Number
while True:
        try:
            ccnum = input('Credit Card Number ')
            ccnum = int(ccnum)
            break
        except ValueError:
            print('Input invalid, please enter only numbers with no spaces.')

# Get Credit Card Number Length
cclength = getLength(ccnum)

# Check if A Valid CC Number Length
validLengths = [13, 15, 16]
if cclength not in validLengths:  # if not correct length, print INVALID
    print('INVALID')
else:
    checksum = calculateChecksum(ccnum)   # Calculate Checksum
    if getLastDigit(checksum) == 0:       # Validate checksum, if Valid...
        firstdigit = getFirstDigit(ccnum)
        first2digits = getFirst2Digits(ccnum)
        if firstdigit == 4:               # Check if first digit is 4
            print('VISA')
        elif first2digits == 34 or first2digits == 37:  # check first two digits
            print('AMEX')
        elif first2digits > 50 and first2digits < 56:
            print('MASTERCARD')
        else:
            print('INVALID')
    else:
        print('INVALID')