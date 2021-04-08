'''
Properties provide a way of customizing access to instance attributes.
They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead.
One common use of a property is to make an attribute read-only.
'''

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property #used to set the decorater above the method.
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True | Can't set attribute appears as it's a read-only attribute


'''
--------------------------------------------------------------------------------------------------------
Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
The same applies to defining getter functions.
'''

class Pizza1:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter #defines the setter for setting a value, same structure for .getter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Nick":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza1(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

"""
---------------------------------------------------------------------------------------------------------
"""

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
    
    @property
    def isAlive(self):
        while self._lives > 0:
            return True
            
# This is code using a while loop for the player using the hit function to decrease lives to 0 then using the propery for isAlive to return True until the player reaches 0 lives, where it then prints "Game Over" and breaks the while loop

p = Player("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break

      