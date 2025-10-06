#!/usr/bin/env python3
# example workign with conditionals
#By Ed Goad
# date: 2/3/2021

# Suggestion - 
#   add in <, ==, > one at a time
#   make each of them if statements initially
#   Change x and y values to test the various paths
#   eventually simplfy with if, elif, else
question = 0
while question == 0:
    dayQuality = input("is today a good day? (y/n): ")
    if dayQuality == "y":
        print("yeah it is :)")
        question = 1
    elif dayQuality == "n":
        print("sorry to hear that")
        question = 1
    else:
        print("Input not recognized please try again")