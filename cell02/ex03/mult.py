#!/usr/bin/env python3
first_num = int(input("Enter the first number:\n"))
second_num = int(input("Enter the second number:\n"))
result = first_num * second_num
print(f"{first_num} x {second_num} = {result}")
if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")