# FUNCTION DEFINITIONS

def getLength(int):
    '''
    accepts an integer, returns the number of digits in that integer
    '''
    length = 0
    while int != 0:
        int = int / 10
        length += 1
    return length

def getLastDigit(int):
    '''
    accepts an integer, returns the last digit of that integer
    '''
    return (int % 10)

def shorten(int):
    '''
    accepts an integer, returns the same integer with the last digit removed
    '''
    return (int / 10)

def getFirstDigit(int):
    '''
    accepts an integer, returns the first digit of that integer
    '''
    intLength = getLength(int)
    for x in range(intLength-1):
        int = shorten(int)
    return int

def getFirst2Digits(int):
    '''
    accepts an integer, returns the first two digits of that integer
    '''
    intLength = getLength(int)
    for x in range(intLength-2):
        int = shorten(int)
    return int

def calculateChecksum(ccnum):
    sum = 0
    ccnumb = ccnum
    for x in range(cclength):
        sum += getLastDigit(ccnumb)             # add last digit to sum
        ccnumb = shorten(ccnumb)                # shorten ccnumb by 1
        nextnum = (getLastDigit(ccnumb)) * 2    # get last digit, multiply by 2
        lastdigitlength = getLength(nextnum)    # get length of lastdigit
        if lastdigitlength == 1:                # if one digit, add to sum
            sum += nextnum
        else:                                   # otherwise
            sum += getLastDigit(nextnum)        # get the last digit of nextnum, add it to sum
            nextnumshorter = shorten(nextnum)   # shorten by 1
            sum += getLastDigit(nextnumshorter) # get last digit, add it to sum
        ccnumb = shorten(ccnumb) # shorten ccnumb by 1

# Get Credit Card Number
while True:
        try:
            ccnum = input('Credit Card Number ')
            ccnum = int(ccnum)
            break
        except ValueError:
            print('Input Invalid, please enter only numbers with no spaces.')

# Get Length of Credit Card Number
cclength = getLength(ccnum)

# Check if A Valid CC Number Length, if not, print INVALID
validLengths = [13, 15, 16]
if cclength not in validLengths:
    print('INVALID')
else:
    # Calculate Checksum
    sum = 0
    ccnumb = ccnum
    for x in range(cclength):
        sum += getLastDigit(ccnumb)             # add last digit to sum
        ccnumb = shorten(ccnumb)                # shorten ccnumb by 1
        nextnum = (getLastDigit(ccnumb)) * 2    # get last digit, multiply by 2
        lastdigitlength = getLength(nextnum)    # get length of lastdigit
        if lastdigitlength == 1:                # if one digit, add to sum
            sum += nextnum
        else:                                   # otherwise
            sum += getLastDigit(nextnum)        # get the last digit of nextnum, add it to sum
            nextnumshorter = shorten(nextnum)   # shorten by 1
            sum += getLastDigit(nextnumshorter) # get last digit, add it to sum
        ccnumb = shorten(ccnumb) # shorten ccnumb by 1

