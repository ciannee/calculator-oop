class UserInterface:
    def try_again(self):
        simple_calculator = input("\nDo you want to try again? ")
        return simple_calculator

    def ask_name(self):
        name = input("\n\033[01mPlease enter your name: ")
        return name
    
    def display_intro(self, name):
        print("\nHi,", name, "I have prepared a simple calculator for you!")

    def ask_operation(self):
       operation = input("\n\033[01m\nPlease choose among the four math operations:\n\nAddition\nSubtraction\nMultiplication\nDivision\n\nEnter your answer: ")
       return operation

    def display_instruction(self):
        print ("\n\nGreat! Please enter two numbers of your choice!")

    def ask_number(self):
       num = float(input("Input a number: "))
       return num
    
    def display_addition(self, num1, num2):
        print("\nWe'll be performing addition on", num1, "and", num2)
    
    def display_sum (self, sum):
        print ("Result: " + str(sum))
    
    def display_subtraction(self, num1, num2):
        print("\nWe'll be performing subtraction on", num1, "and", num2)
    
    def display_difference(self, difference):
        print ("Result: " + str(difference))
    
    def display_multiplication(self, num1, num2):
        print("\nWe'll be performing multiplication on", num1, "and", num2)
    
    def display_product(self, product):
        print ("Result: " + str(product))
    
    def display_division(self, num1, num2):
        print ("\nWe'll be performing division on", num1, "and", num2)
    
    def display_quotient(self, quotient):
        print ("Result: " + str(quotient))
    
    def display_yes(self, starting):
        print("STARTING.....")