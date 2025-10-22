#!/usr/bin/env python3
# Sample script that writes to a file
#by Isaac Stewart

import os

name = input("What is your name?: ")
color = input("What is your favorite color?: ")
petName = input("What is your pet's name?: ")
maidenName = input("What is your mother's maiden name?: ")
elementary = input("What elementary school did you attend? ")

hack_file = open("hackme.txt", "w")

hack_file.write(name)
hack_file.write("\n")
hack_file.write(color)
hack_file.write("\n")
hack_file.write(petName)
hack_file.write("\n")
hack_file.write(maidenName)
hack_file.write("\n")
hack_file.write(elementary)

hack_file.close()