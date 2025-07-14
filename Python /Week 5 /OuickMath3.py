#1. Create a class called calculator
#2. Create a function in the class for each mathematical operation: Addition, Multiplication, Division, Subtraction
#3. Outside of your class definition, create an instance of your calculator class
#4. Call each function in your calculator class and store each output into a variable. Use any values for arguments.
#5. Print all your variables to the console



class Calculator:
    def Add(self, x, y):
        return x + y
      
    def Subtraction(self, x, y):
        return  x - y 
    
    def Multiplication(self, x, y):
        return x * y
    
    def Division(self, x, y):
        return x / y 

calculator = Calculator()

sum = calculator.Add(25, 78)
different = calculator.Subtraction(35, 20)
product = calculator.Multiplication(30, 7)
dividend = calculator.Division(40, 6)

print(sum)
print(different)
print(product)
print(dividend)

    