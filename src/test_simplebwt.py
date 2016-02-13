# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:33:54 2016

@author: frizio
"""

# Useful for iPython console in Spyder IDE: 
# del all variables in workspace and clean the screen
from IPython import get_ipython
get_ipython().magic('reset -sf')
get_ipython().magic('clear')


# Test BWT

def myprint(t, l):
    print(t)    
    print(l)
    print(" ")


def mylistprint(t, l):
    print(t)    
    for i in l: 
        print(i)
    print(" ")
    

# Simplest Burrows-Wheeler transform implementation

s = input("Enter the input string: ") or "abraca"
myprint("Input string: ", s)

#s += "\0"
eos = "$"

print("Perform 'verbose' and non-efficient Burrows-Wheeler transformation")
print("O(n^2) respective to the length of the input string" + "\n")

rotations = [s[i:] + s[:i] for i in range(len(s))]
mylistprint("Cyclic shift of s", rotations)

table = sorted(rotations)
mylistprint("Sorted cyclic shift", table)

# Extract the last characters of each row
last_column = [row[-1] for row in table]
myprint("Last column: ", last_column)

r = "".join(last_column)
myprint("BW trasformation of input string: ", r)

del rotations, table, last_column

print("####################################################" + "\n")

# Simplest Inverse Burrow-Wheeler transform implementation.

print("Perform 'verbose' Inverse Burrows-Wheeler transformation" + "\n")


table = [""] * len(r)
        
# Use lf-mapping to reverse the tranformation
for i in range(len(r)):

    # add one letter for each partial string in the suffix array
    prepended = [r[i] + table[i] for i in range(len(s))]
    print("STEP: " + str(i), "\n")
    mylistprint("First Column insertion", prepended) 
    
    # convert it to sorted suffix array
    table = sorted(prepended)
    mylistprint("Sorting rows", table) 

del s   
s = ""
# Find the correct row (ending in "\0")
for row in table:
    if row.endswith(eos):
        s = row
        break

# Get rid of trailing null character
s = s.rstrip(eos)
myprint("Original string: ", s)

print("####################################################" + "\n")


