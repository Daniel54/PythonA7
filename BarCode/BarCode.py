#!/usr/bin/env python3

import sys

def printdigit(d):
    """
    Prints the digits as a barcode
    Args
        d -> the digit to be printed
    """
    pass

def printBarCode(zipcode):
    """
    Validates input and parses zipcode numbers
    Args
        zipcode -> the zipcode to be parsed. A zipcode
                   is a string of 5 numbers
    """
    print(zipcode)

def main():
    """
    Main funcion
    """

    #throws index error if empty
    printBarCode(sys.argv[1])

if __name__== "__main__":
    main()
    exit(0)



