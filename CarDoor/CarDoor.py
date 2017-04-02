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
    LDoorOpen = False
    RDoorOpen = False
    
    #Order:(below)
    #LD RD Cl ML LI LO RI RO GS
    str = str.replace(" ", "")
    str = str.strip('\n')
    
    #returns list of 10 el:
    #last 9 are commands
    comndList = str.split(",")
    
    #set variables and cast to ints
    LD = int(comndList[1])
    RD = int(comndList[2])
    CL = int(comndList[3])
    ML = int(comndList[4])
    LI = int(comndList[5])
    LO = int(comndList[6])
    RI = int(comndList[7])
    RO = int(comndList[8])
    GS = comndList[9]

    #print output 
    print("LD Left dashboard switch (0 or 1): ", LD)
    print("RD Right dashboard switch (0 or 1):", RD)
    print("CL Child Lock switch (0 or 1): ", CL)
    print("ML Master unlock switch (0 or 1): ", ML)
    print("LI Left inside handle (0 or 1): ", LI)
    print("LO Left outside handle (0 or 1): ", LO)
    print("RI Right inside handle (0 or 1): ", RI)
    print("RO Right outside handle (0 or 1): ", RO)
    print("GS Gear shift position (P, N, D, 1, 2, 3, or R): ", GS)
    print("")

    ###########################run checks
    
    if CL == 1: #if child lock on then switch R and L inside handles off
        LI = 0
        RI = 0
        print("Child lock is on")
    #Validate GS input. if NOT any of the valid options (P N D 1 2 3 R)
    if not (GS == "P" or GS == "N" or GS == "D" or GS == "1" or GS == "2" or GS == "3" or GS == "R"):
        print("Invalid Record: Both Doors stay closed")
    else:#only if valid gear shift, trip other swithces
        print("Befor Switches")
        print("Left Door var: ", LDoorOpen)
        print("Right Door var: ", RDoorOpen)

        if GS == "P" and ML == 1:
        #check switches
            if LD == 1:
                LDoorOpen = True
            if RD == 1:
                RDoorOpen = True
            if LI == 1:
                LDoorOpen = True
            if LO == 1:
                LDoorOpen = True
            if RI == 1:
                RDoorOpen = True
            if RO == 1:
                RDoorOpen = True

        print("After switches")
        print("Left Door var: ", LDoorOpen)
        print("Right Door var: ", RDoorOpen)
        print("")
    #Check Door Status and output message
    #2 options that are binare (so 2^2 only leaves 4 different options)
    if LDoorOpen == True and RDoorOpen == True:
        print("Booth Doors Open")

    elif LDoorOpen == False and RDoorOpen == False:
        print("Booth Doors stay closed")

    elif LDoorOpen == True:
        print("Left Door open")

    elif RDoorOpen == True:
        print("Right Door open")
    #Note: Bug: orignal checks where chained if statements. Behavoir was incorrect.
    #Fix: Replaced chained ifs with if elif statement. Corrected the output.
    print("")
    print("")
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
    for i in range(len(commands)):
        if( i != 0): #skip first index
            check_string(commands[i])

    print("Length of command: ",len(commands))

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

