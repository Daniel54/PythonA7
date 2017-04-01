#!/usr/bin/env python3
import sys
import re
from urllib.request import urlopen

url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv"

def check_string( str ):
    """
    Checks a given string by spliting.
    Args: <str> the string to be checked
    """
    #LD RD Cl ML LI LO RI RO GS
    print(str)
    str = str.replace(" ", "")
    str = str.strip('\n')
    print("striped: ", str)
    
    #returns list of 10 el:
    #last 9 are commands
    comndList = str.split(",")

    LD = comndList[1]
    RD = comndList[2]
    Cl = comndList[3]
    ML = comndList[4]
    LI = comndList[5]
    LO = comndList[6]
    RI = comndList[7]
    RO = comndList[8]
    GS = comndList[9]
    
    print(comndList)



def get_file( url ):
    """
    Takes in a url and fetcheds the file
    Args: <url> the url to fetch
    """

    with urlopen(url) as cmnds:
        commands = []
        for row in cmnds:
            line = row.decode("utf-8")
            #add each line to commands: "R1 0, 0, etc..."
            commands.append(line)

    #loop through commands (using range of length of commands)
        #skip first row
        #split each string
        #check according to possiton of the string
    #loop through and skip the first. 
    for i in range(len(commands)):
        if( i != 0): #skip first index
            check_string(commands[i])

    print("Length of command: ",len(commands))
    #print("Type of Command", type(commands))
    #print("Index 2 of Commands: ", commands[2])
    #print("Index 2 type Commands: ", type(commands[2]))
    #theString = commands[1]
    #splitUp = theString.split(",")
    #print(splitUp)
    #print("Tpye of splitUp: ", type(splitUp))

def main():
    """
    Main funcion
    """
    get_file(url)
    pass

if __name__== "__main__":
    main()
    exit(0)


#exit(0)

