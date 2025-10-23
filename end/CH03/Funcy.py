#!/usr/bin/env python3
# example workign with Loops
##By Isaac Stewart

def send_message():
    for x in range(10):
            print("yeah it is :)")
    

question = 0
while question == 0:
    dayQuality = input("is today a good day? (y/n): ")
    if dayQuality == "y":
        send_message()
        question = 1
    elif dayQuality == "n":
        print("sorry to hear that")
        question = 1
    else:
        print("Input not recognized please try again")