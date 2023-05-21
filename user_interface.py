class UserInterface:
    def ask_input(self):
       operation = input("\n\033[01m\nPlease choose among the four math operations:\n\nAddition\nSubtraction\nMultiplication\nDivision\n\nEnter your answer: ")
       return operation

       num = float(input("Input a number: "))
       return num
    