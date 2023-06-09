# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 7: Redo calculator using OOP concept

from user_interface import UserInterface
from calculator import Calculator
from calculator_patricia import CalculatorPatricia
import time

# while loop
simple_calculator = ""
while simple_calculator != "NO":

    ui = UserInterface()
    calc = Calculator()
    patricia = CalculatorPatricia()

    # Pseudocode

    # ask user for name
    name = ui.ask_name()
    time.sleep(3)
    ui.display_intro(name)
    time.sleep(3)

    # ask user for input (math operations)
    operation = ui.ask_operation()
    time.sleep(2)
    ui.display_instruction()

    # ask user for 1st number
    num1 = ui.ask_number()

    # ask user for 2nd number
    num2 = ui.ask_number()

    # addition
    if operation.upper() == "ADDITION":
        ui.display_addition(num1, num2)
        ui.display_loading_screen()
        sum = calc.add(num1, num2)
        ui.display_sum(sum)

    # subtraction
    elif operation.upper() == "SUBTRACTION":
        ui.display_subtraction(num1, num2)
        ui.display_loading_screen()
        difference = calc.subtract(num1, num2)
        ui.display_difference(difference)

    # multiplication
    elif operation.upper() == "MULTIPLICATION":
        ui.display_multiplication(num1, num2)
        ui.display_loading_screen()
        product = calc.multiply(num1, num2)
        ui.display_product(product)

    # division
    elif operation.upper() == "DIVISION":
        ui.display_division(num1, num2)
        ui.display_loading_screen()
        quotient = calc.divide(num1, num2)
        ui.display_quotient(quotient)
    
    elif operation.upper() == "EXPONENT":
        ui.display_power_rule(num1, num2)
        ui.display_loading_screen()
        exponent = patricia.exponent(num1, num2)
        ui.display_exponent(exponent)
    

    # ask user to try again
    simple_calculator = ui.try_again()
    
   # if yes
    if simple_calculator.upper() == "YES":
        time.sleep(2)
        print("STARTING.....")

    # if no
    else: 
        simple_calculator.upper() == "NO"
        time.sleep(2)
        print("THANK YOU!")
        break