import math
class Calculator:
    def power(self, a, b):
        return a ** b

    def modulo(self, a, b):
        return a % b

    def add(self, a, b):
        return round(a + b, 10) # fix
    
    def subtract(self, a, b):
        result = a - b

        if math.isinf(result):
            raise OverflowError("Result is too large to represent")

        return result

    def multiply(self, a, b): 
        if type(a) not in (int, float) or type(b) not in (int, float): # fix
            raise TypeError("Inputs must be numbers")
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        return int(result) if result.is_integer() else result
