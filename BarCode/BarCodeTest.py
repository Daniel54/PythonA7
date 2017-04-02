#!/usr/bin/env python3

import sys
import BarCode
from urllib.request import urlopen


def test_barcode(url):
    """
    fetches a url containing a list of barcodes
    Args
        url -> url to list of barcodes
    """

    #default url for testing if one isn't supplied
    l = []
    with urlopen(url) as inFile:
        for line in inFile:
            #BarCode.printBarCode(line.decode('utf-8'))
            l.append(line.decode('utf-8').rstrip())
    for x in l:
        BarCode.printBarCode(x)


def main():
    """
    main for testing
    """
    
    url = 'http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt'

    try:
        test_barcode(sys.argv[1])
    except IndexError:
        print("No url supplied. Using default.")
        #continue program with default url
        test_barcode(url)


if __name__ == "__main__":
    main()
    exit(0)

