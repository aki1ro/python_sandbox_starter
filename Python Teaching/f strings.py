#F Strings are used to create strings.

name = "Nick"

age = 21

ex1= "my name is " + name + " and I am " + str(age) + " years old"

ex2 = "my name is {0} and I am {1} years old".format(name, age)

ex3 = "my name is %s and I am %i years old" %(name, age)

ex4 = f"my name is {name} and I am {age + 7} years old"
# start an f string with f or F and " and or ', put any variables or expression into curly braces. 

print(ex1)
print(ex2)
print(ex3)
print(ex4)

