
class GeekforGeeks: 
 
    # default constructor 
    def __init__(self): 
        self.geek = "GeekforGeeks"
  
    # a method for printing data members 
    def print_Geek(self): 
        print(self.geek)
    def math_Geek(self, x, y):
        print(x + y)
        
obj = GeekforGeeks()

print(obj.print_Geek())

class Addition: 
    first = 0
    second = 0
    answer = 0
      
    # parameterized constructor 
    def __init__(self, f, s): 
        self.first = f 
        self.second = s
        
      
    def display(self): 
        print("First strings = " + str(self.first)) 
        print("Second strings = " + str(self.second)) 
        print("Addition of two strings = " + str(self.answer)) 
  
    def calculate(self): 
        self.answer = self.first + self.second 
  
# creating object of the class 
# this will invoke parameterized constructor 
first = int(input())
second = int(input())

# obj = Addition(first, second) 

# # perform Addition 
# obj.calculate() 

# # display result 
# obj.display() 

Addition.display