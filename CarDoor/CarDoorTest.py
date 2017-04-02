#!/usr/bin/env python3
from CarDoor import check_string
import sys
from urllib.request import urlopen

def get_file( url ):
    """
    Takes in a url and fetcheds the file
    Args: <url> the url to fetch
    """

    with urlopen(url) as cmnds:
        commands = []
        for row in cmnds:
            line = row.decode("utf-8")
            commands.append(line)

    for i in range(len(commands)): 
        if( i != 0): #skip first index
            print("Reading Record: ", i)
            check_string(commands[i])


def main():
    """
    Main funcion
    """
    url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv"
    get_file(url)
    pass

if __name__== "__main__":
    main()
    exit(0)


#exit(0)

