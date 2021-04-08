try:
   num1 = 7
   num2 = 0
   print(num1/num2) #This will give the ZeroDivisonError
except ZeroDivisionError:
   print("ZeroDivisionError Occured, this except statement is telling you this using print function")
'''
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program.
'''

'''
Different exceptions are raised for different reasons.
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
'''

'''
Python has several other built-in exceptions, such as ZeroDivisionError( as in example above(print(num1/num2)) and OSError. Third-party libraries also often define their own exceptions.
'''
#you can use the try/except statement to create code that may throw and exception that except will then handle 

try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

#Code above declares that if ZeroDivisonError occurs then do this, this being the print functions below.

try:
   x = 2
   y = 0
   z = "Nick"
   print(x + y)
   print(x / y)
   print(z + y)
   print("Nick" + z)
except (ZeroDivisionError, TypeError):
   print("Error Has Occured")

print(f"Finished try/except statement using the following variables:{x,y,z}")

'''
------------------------------------------------------------------------------------------------
If you want to create a try/except statement where except catches everything error, just use except: Becareful using this, as it will hide programming mistakes that would normally show via a debugger.
'''
try:
   m = 3
   b = "Nick"
   c = 2.1

   print(m, b, c)
   print(m + b)
   print(c - 0)

except:
   print("Some Error has occured...not sure what though")

'''
--------------------------------------------------------------------------------------------------------
a finally block can follow after a try/except statement. It will execture after the try/except block, no matter if an exception occured or not
'''
try:
   print("e" + 0)
except:
   print("no no no")
finally:
   print("the finally block no no no")

'''
The finally block is useful, for example, when working with files and resources: it can be used to make sure files or resources are closed or released regardless of whether an exception occurs.
'''

'''
---------------------------------------------------------------------------------------------------------
You can also use an else statement with a try/except statement. the else statement only occurs if the try statement does. 
'''

# try:
#    print(1 + 3)
# except:
#    (print("error here"))
# else:
#    print(1 + 2)

x = 3

y = 4

z = x + y

try:
   if z == x + y:
      print("Equal Variables")
   print(z + "Nick") #Take this out to make the statement try true and thus else is true as well. Even if the If statement doesn't run true aka run the print function it will still be true in regards to no errors occuring within the code. Thus the try statement is true and the else statement will still run
except:
   print(f"I printed z here now error occured {z}")
else:
   print(x + y + z)


# num = 100
# if num == 100:
   # raise SyntaxError("I made this up lol") #type of exception that has occured. ValueError, TypeError, SyntaxError you can also give details about the erorr as well for other developers to understand


#Random event: Given I have 10 apples: I run a program that lets me remove or add apples using the "remove" and "add" functions defined below, but when I remove apples I lose 2 apples, or I choose to add apples then I gain 3 apples. This program has to be run through a try/expect statement that will raise an error if apples > 15 or < 5 with the string "You have gone Above 15 or Below 5 CURRENT APPLES:" and the variables apples appended . If the input is not "add" or "remove" it should return a string with "Enter 'remove' or 'add' please", else it should give the left over apples as the string "Your left over apples:" with the variables apples appended. Also give the program 5 times to input either "add" or "remove" to adjust the number of the variable apples. *Use any errors for the except statements. 

def add(a):
   a += 3
   return a

def remove(a):
   a -= 2
   return a

#your code here:

try:
   apples = 10
   i = 0
   while i < 5:
      x = input()
      if x == "add":
         apples = add(apples)
         if apples < 5 or apples > 15:
            raise EOFError
      elif x == "remove":
         apples = remove(apples)
         if apples < 5 or apples > 15:
            raise EOFError
      elif x != "remove" or "add":
            raise ValueError
      print(apples)
      
      i += 1

except EOFError:
   print(f"You have gone Above 15 or Below 5 CURRENT APPLES: {apples}")
except ValueError:
   print("Enter 'remove' or 'add' please")


else:
   print(f'Your left over apples: {apples}')








