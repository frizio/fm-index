# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:33:54 2016

@author: frizio
"""

# Useful for iPython console in Spyder IDE: 
# del all variables in workspace and clean the screen
from IPython import get_ipython
get_ipython().magic('reset -sf')
get_ipython().magic('clear')

from pprint import pprint

def myprint(t, l):
    print(t)    
    print(l)
    print(" ")

def mypprint(t, l):
    print(t)    
    pprint(l)
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
EOS = "$"
s += EOS

print("Perform 'verbose' suffix array Burrows-Wheeler transformation" + "\n\n")

rotations = [ s[i:] for i in range(len(s)) ]
# Instead of [ s[i:] + s[:i] ... ]
mylistprint("Suffix of the input string", rotations)

rotations.sort()
mylistprint("Sorting suffix", rotations)

k = len(rotations)

sa = [0] * k
tmp = [0] * k

for i in range(k):
    l = len(rotations[i])
    sa[i] = k - l
    if l == k:
        tmp[i] = EOS
    else:
        tmp[i] = s[-l-1]

myprint("tmp", tmp)
myprint("Suffix array sa: ", sa)

r = ''.join(tmp)
myprint("BW trasformation of input string: ", r)


print("####################################################" + "\n")


print("Perform 'verbose' Inverse Burrows-Wheeler transformation")
print("Using LF-Mapping" + "\n")

import bwt

# Calculate the first occurance of letters in left (first) column
occ = bwt.calc_first_occ(r)
mypprint("first occ: ", occ)

# Calculate the full lf-mapping
# lf is mapping from input letter rank occurance to left letter
# this shows for which idx in last column corresponds to the first idx
lf = [0] * len(r)
myprint("LF: ", lf)
for i, c in enumerate(r):
    print(i, c)
    lf[i] = occ[c]
    print(lf)
    occ[c] += 1
del occ
print(" ")
myprint("LF: ", lf)

myprint("BW trasformation of input string: ", r)

# s is the original string
del s
s = [''] * (len(r)-1)
myprint("s initial: ", s)

# follow the lf mapping until we have the full string
i = 0
for k in range(len(s)-1,-1,-1):
    print("i=", i)
    s[k] = r[i]
    print(s)
    i = lf[i]
myprint("s final: ", s)

# convert it to a string
s = ''.join(s).rstrip(EOS)
myprint("Original string: ", s)