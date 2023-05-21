# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 7: Redo calculator using OOP concept

from user_interface import UserInterface
from calculator import Calculator

# while loop
simple_calculator = ""
while simple_calculator != "NO":

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
    if operation.upper() == "MULTIPLICATION":
        ui.display_multiplication(num1, num2)
        product = calc.multiply(num1, num2)
        ui.display_product(product)

    # division
    if operation.upper() == "DIVISION":
        ui.display_division(num1, num2)
        quotient = calc.divide(num1, num2)
        ui.display_quotient(quotient)
    
    simple_calculator = ui.try_again()
    
    # if yes
    if simple_calculator.upper() == "YES":
        
    # if no
    else: 
        simple_calculator.upper() == "NO"
        
        break