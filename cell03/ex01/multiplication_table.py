#!/usr/bin/python3
number = input("Enter a number\n")
try:
    val = int(number)
except ValueError:
    print("That's not an int!")
else:
    start = 0
    while (start <= 9):
        result = start * int(number)
        print(f"{start} x {number} = {result}")
        start += 1
