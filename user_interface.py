class UserInterface:
    def ask_operation(self):
       operation = input("\n\033[01m\nPlease choose among the four math operations:\n\nAddition\nSubtraction\nMultiplication\nDivision\n\nEnter your answer: ")
       return operation

    def ask_number(self):
       num = float(input("Input a number: "))
       return num
    
    def display_addition(self, num1, num2):
        print("\nWe'll be performing addition on", num1, "and", num2)
    
    def display_sum (self, sum):
        print ("Result: " + str(sum))