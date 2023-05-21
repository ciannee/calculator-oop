# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 7: Redo calculator using OOP concept

from user_interface import UserInterface
from calculator import Calculator

ui = UserInterface()
calc = Calculator()

# Pseudocode

# ask user for input (math operations)
operation = ui.ask_operation()

# ask user for 1st number
num1 = ui.ask_number()

# ask user for 2nd number
num2 = ui.ask_number()

# addition
if operation.upper() == "ADDITION":
    ui.display_addition(num1, num2)
    sum = calc.add(num1, num2)
    ui.display_sum(sum)

# subtraction
if operation.upper() == "SUBTRACTION":
    ui.display_subtraction(num1, num2)
    difference = calc.subtract(num1, num2)
    ui.display_difference(difference)

# multiplication
product = calc.multiply(num1, num2)

# division
quotient = calc.divide(num1, num2)
