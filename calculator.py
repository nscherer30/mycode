#!/usr/bin/env python3
# Make a calculator that takes two integers and adds/subtracts/divides/multiplies them!
# Use FUNCTIONS to create a calculator! Your script must accept the following user input:
#
# a float/integer
# another float/integer
# an operator (add, subtract, divide, multiply)
# Your script should return the answer!
#
# BONUS 1: Make the script human-error proof. Use IF/ELIF/ELSE and TRY/EXCEPT where necessary!
#
# BONUS 2: If the user types in a bad input, have them type it in again! Use a WHILE LOOP!
#
# Upload your script to GitHub and send Chad the link in-chat! Once Chad's confirmed it, you may call it a night!

class Calculator():

    def __init__(self, ):
        pass

    def compute(self, num_one, num_two, operator):
        try:
            answer = eval(num_one + operator + num_two)
        except ZeroDivisionError:
            answer = "undefined"
        finally:
            print(f"{num_one} {operator} {num_two} = {answer}")

def check_num_input(number_as_string):
    err_msg = "You did not enter a integer or float, try again."
    if len(number_as_string) < 1:
        print(err_msg)
        return False
    try:
        float(number_as_string)
    except ValueError:
        print(err_msg)
        return False
    return True

def check_operator_input(operator):
    err_msg = "You did not enter a valid operator, try again."
    if operator == "+" or operator == "-" or operator == "/" or operator == "*":
        return True
    print(err_msg)
    return False

def main():
    while True:
        input_one = input(f"Enter a number (float or integer): ").strip()
        if check_num_input(input_one):
            break

    while True:
        input_two = input(f"Enter a second number (float or integer): ").strip()
        if check_num_input(input_two):
            break

    while True:
        operator = input(f"Enter an operator (+, -, /, *): ").strip()
        if check_operator_input(operator):
            calc = Calculator()
            calc.compute(input_one, input_two, operator)
            break

if __name__ == '__main__':
    main()

