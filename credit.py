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
    for x in range(intLength):
        int = shorten(int)
    return int

def getFirst2Digits(int):
    '''
    accepts an integer, returns the first two digits of that integer
    '''
    intLength = getLength(int)
    for x in range(intLength-1):
        int = shorten(int)
    return int

