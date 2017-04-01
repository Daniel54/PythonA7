#!/usr/bin/env python3

import sys


#dictionary to store the barcode pictograms
picto = {'1':':::||', '2':'::|:|', '3':'::||:', '4':':|::|', '5':':|:|:', '6':':||::', '7':'|:::|', '8':'|::|:', '9':'|:|::', '0':'||:::'}


def printDigit(d):
    """
    Takes a singular digit and encrypts it as a barcode segment
    Args
        d -> the digit to be printed
    Returns
        the pictogram string representing the input number
    """
    global picto
    return picto[str(d)]


def printBarCode(zipcode):
    """
    Validates input and parses zipcode numbers
    Args
        zipcode -> the zipcode to be parsed. A zipcode
                   is a string of 5 numbers
    """
    code = []
    code.append('|') #opening guard bar
    code = [printDigit(x) for x in zipcode]
    code.append(computeCheckDigit(zipcode))
    code.append('|') #ending guard bar
    print(''.join(code))


def computeCheckDigit(zipcode):
    """
    Computes the check digit for the zipcode by using a weight of 7,4,2,1,0.
    The checkDigit is the digit that difference between a number divisible
    by 10 and our weighted number. 
    Args
        zipcode -> the zipcode to encode with a check digit
    Returns
        the pictogram string representing the input number
    """
    
    #zipcode has to be 5 num in length
    #calculates the checkDigit by using weights
    #takes the result and modulo 10
    #subtract that result to get checkDigit
    checkDigit = 7 * int(zipcode[0]) +4 * int(zipcode[1]) + 2 * int(zipcode[2]) + 1 * int(zipcode[3]) + 0 * int(zipcode[4])
    
    checkDigit %= 10
    checkDigit = 10 - checkDigit
    return printDigit(checkDigit)


def main():
    """
    Main funcion
    """

    #throws index error if empty
    printBarCode(sys.argv[1])

if __name__== "__main__":
    main()
    exit(0)



