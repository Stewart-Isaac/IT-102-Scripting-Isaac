#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created by Isaac Stewart
print("Hello World")

#prompts the user for their name
your_name = input("Please enter your name: ")
print("Hello ", your_name)
if your_name == "Isaac":
    print("Nice name dummy")
else:
    print("My name is Isaac")

print("Today is going to be a great day")

age = input("Please enter your age: ")
age2years = int(age) + 2
print("You will be", age2years, "in 2 years")
