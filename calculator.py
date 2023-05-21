class Calculator:
    def add(self, num1, num2):
        sum = num1 + num2
        return sum
    
    def subtract(self, num1, num2):
        difference = num1 - num2
        return difference
    
    def multiply(self, num1, num2):
        product = num1 * num2
        return product
    
    def divide(self, num1, num2):
        try:
            quotient = (float(num1) / float(num2))
        except ZeroDivisionError:
            quotient = 0
        finally:
            return quotient