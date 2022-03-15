#! /usr/bin/python3

var = int(input("Enter an integer: "))

if var > 99:
    print("big number")
elif var > 9:
    print("two-digit number")
elif var < 0:
    print("negative number")
elif var == 0:
    print("zero")
else:
    print("single-digit number")