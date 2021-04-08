# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

'''
print("Hellow Josh")

feeling = input("How are you feeling today: ")
print("That's great you're feeling " + feeling)
'''

x = 1                           # int
y = 2.4                         # float
z = 8.8                         # float
name = 'Jefferson the 3rd'      # string
gender = "Male"                 # string
is_verified = False             # bool (boolean)
is_cool = True                  # bool (boolean)
print (x, y, name, is_cool)

# Multiple assignment
x, y, name, is_cool = (1, 4.2, 'Nick', True)

print (x, y, name, is_cool)

# Basic math
a = x + y
print(a)

# Casting
x = str(x)          #this is casting (changing data class) x (int) into string (str)
y = int(y)
z = float(y)

#check type
print(type(y))              #shows data class for y
print(type(x))              #shows data class for x
print(type(z))              #shows data class for z
print(z)

u = 88

print("this is u:", u%9)

u = 108

print("now u is 108 so answer differs:", u%11)
