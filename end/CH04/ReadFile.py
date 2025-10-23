#!/usr/bin/env python3
# Sample script that reads from a file
# By Ed Goad
# 12/12

import os



hackfile = open("hackme.txt", "r")

name = hackfile.readline()
color = hackfile.readline()
petname = hackfile.readline()
maiden = hackfile.readline()
elementary = hackfile.readline()

print("Here is someone to hack - information:")
print("name: ", name)
print("Fav color: ", color)
print("Pet name: ", petname)
print("Mother's maiden name: ", maiden)
print("elementary school: ", elementary)

hackfile.close()
