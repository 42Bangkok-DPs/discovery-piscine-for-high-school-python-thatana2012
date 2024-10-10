#!/usr/bin/env python3
number = int(input("Enter a number\n"))
start = int(0)
while (start <= 9):
    result = start * number
    print(f"{start} x {number} = {result}")
    start += 1
