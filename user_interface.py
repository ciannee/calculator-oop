import time

class UserInterface:
    def try_again(self):
        simple_calculator = input("\nDo you want to try again? ")
        return simple_calculator

    def ask_name(self):
        name = input("\n\033[01mPlease enter your name: ")
        return name
    
    def display_intro(self, name):
        print("\n\033[93mHi,", name, "I have prepared a simple calculator for you!")

    def ask_operation(self):
       operation = input("\n\033[01m\nPlease choose among the four math operations:\n\nAddition\nSubtraction\nMultiplication\nDivision\n\nEnter your answer: ")
       return operation

    def display_instruction(self):
        print ("\n\n\033[33mGreat! Please enter two numbers of your choice!")

    def ask_number(self):
       num = float(input("Input a number: "))
       return num
    
    def display_loading_screen(self):
        print("\n\033[36mSTARTING..........")
        time.sleep(3)
        print("\n  █▒▒▒▒▒▒▒▒▒")
        time.sleep(1)
        print("\n  ███▒▒▒▒▒▒▒")
        time.sleep(1)
        print("\n  █████▒▒▒▒▒")
        time.sleep(1)
        print("\n  ███████▒▒▒")
        time.sleep(1)
        print("\n  ██████████")
        time.sleep(3)

    def display_invalid_input(self):
        print("\nInvalid Input!")

    def display_addition(self, num1, num2):
        print("\n\033[92mWe'll be performing addition on", num1, "and", num2)

    def display_sum (self, sum):
        print ("\nResult: " + str(sum))
    
    def display_subtraction(self, num1, num2):
        print("\n\033[36mWe'll be performing subtraction on", num1, "and", num2)
    
    def display_difference(self, difference):
        print ("\nResult: " + str(difference))
    
    def display_multiplication(self, num1, num2):
        print("\n\033[91mWe'll be performing multiplication on", num1, "and", num2)
    
    def display_product(self, product):
        print ("\nResult: " + str(product))
    
    def display_division(self, num1, num2):
        print ("\n\033[95mWe'll be performing division on", num1, "and", num2)
    
    def display_quotient(self, quotient):
        print ("\nResult: " + str(quotient))
    
    def display_yes(self, starting):
        print("STARTING.....")