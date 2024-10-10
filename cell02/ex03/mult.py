#!/usr/bin/python3
first_num = input("Enter the first number:\n")
second_num = input("Enter the second number:\n")
try:
    val1 = int(first_num)
    val2 = int(second_num)
except ValueError:
    print("Error")
else:
    result = int(first_num) * int(second_num)
    print(f"{first_num} x {second_num} = {result}")
    if result < 0:
        print("The result is negative.")
    elif result > 0:
        print("The result is positive.")
    else:
        print("The result is positive and negative.")