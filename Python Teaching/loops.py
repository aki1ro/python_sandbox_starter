# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).



# While loops execute a set of statements as long as a condition is true.


list = ["yo yo yo"]
o = 0

# for x in list:
#    print(x + "OK")

for x in list:
   if x == "yo yo yo":
      o += 1
print(o)

cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0

for price in cart:
    price -= (price*(discount/100))
      
    total += price
    
print(total)
      
print(15*(50/100))

'''
The else Statement Used with Loops
Python supports to have an else statement associated with a loop statements.

If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.
'''

