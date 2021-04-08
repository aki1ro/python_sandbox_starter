'''
Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.
They are marked with the staticmethod decorator.
'''

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
   

    def delicious(self):
       return f"Yummy {self.toppings} Pizza~!"
       
        

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
           return True 
           

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

print(Pizza.validate_topping(ingredients))

print(pizza.delicious())

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @staticmethod
    def area(height, width):
        return height * width

w = int(input())
h = int(input())

print(Shape.area(w, h))

