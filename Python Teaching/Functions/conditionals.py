# If/ Else conditions are used to decide to do something based on something being true or false

x = 6
y = 6

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#Simple if
if x == y:
   print(f'{x} is equal to {y}')
else:
   print("IT WORKS MORTY")

#if/else

if x > y:
   print(f'{x} is greater than {y}')
elif x == y:
   print(f'{x} is equal to {y}')
else:
   print(x, "is less than", y)  

agecutoffsmoke = 18

agecutoffdrink = 21


age = int(input("Are you legal to Drink or Smoke? Enter Age: "))

if agecutoffsmoke <= age:
   age = age   
else:print("You are not legal to Smoke or Drink")

if agecutoffsmoke <= age:
      if agecutoffdrink > age:
         print("You are legal to Smoke, but not Drink")
if agecutoffdrink <= age:
   print("You are legal to Drink and Smoke")

x = int(input("Enter Number here: "))

if x == 1:
   print(x, "equal to 1")
elif x > 1:
   print(x, "not equal to 1")

y = int(input("Enter Number here: "))

if y < 300:
   print(y, "is less than 300")
else:
   if y > 300:
      print(y, "is greater than 300")

year = int(input())

if year % 4 != 0 and year % 100 != 0 and year % 400 !=0:
    print("Not a leap year")
# elif year % 100 != 0:
#     print("Not a leap year")
# elif year % 400 != 0: 
#     print("Not a leap year")
else: 
    print("Leap year")



#Nested if
# if x > 2:
#    if x <= 10:
#       print(f'{x} is less than 2 and greater than 10')

# Logical operators (and, or, not) - Used to combine conditional statements

 


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object




# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# if x is not y:
#    print(f'{x} is not {y}')

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input())

while number != secret_number:
    if number != secret_number:
       print("Ha ha! You're stuck in my loop!")
       number = int(input())
else:
   print("Well done, muggle! You are free now.")
       


# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

word = input()

while word != "chupacabra":
    if word != "chupacabra":
        word = input()
    else:
         break
print("You've successfully left the loop.")