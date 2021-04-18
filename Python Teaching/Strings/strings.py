# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Nick'
age = 28

name1 = 'Josh'
age1 = 28

# Concatenate
print('Hello World ' + 'my name is ' + name + ' and I am ' + str(age))
print('Hello World ' + 'my name is ' + name1 + ' and I am ' + str(age1))

# String Formatting

# Arguments by position

# format for the Arugement = print("{}, {}, {}".format("a", "b", "c"))
print("{2}, {0}, {1}".format("a", "b", "c"))



# Arguments by name
print("My name is {name} and I am {age}".format(name=name, age=age))


# F-Strings

print(f'My name is {name1} and I am {age1}')

# String Methods

s = 'hello there python'

salpha = "alpha"

snumeric = "8808"

# Capitalize first letter
print(s.capitalize() + ' <---- This is first letter Capitalize')


# Make all uppercase
print(s.upper() + ' <---- This is all uppercase')

# Make all lowercase
print(s.lower() + ' <---- This is all lowercase')

# Swap case
print(s.swapcase() + ' <----This is swap case')

# Get length
print(str(len(s)) + ' <----This is the Length')

# Replace
print(s.replace('python', 'vscode') + ' <---- This is replacing words')

# Count
sub = "h"
print(s.count(sub))

# Starts with
print(str(s.startswith('hello there')) + ' <--- checks for sequence from start to end, if any words out of order will print false')

# Ends with
print(str(s.endswith('d')) + ' <--- checks for sequence from end to start, if any words out of order will print false')


# Split into a list
print(str(s.split()) + ' <--- this splits string into lists')

# Find position
print(str(s.find('r')) + ' <--- this finds the position starting from 0 of the string')

# Is all alphanumeric
print(str(s.isalnum()) + "<--- Checks if string is alphanumeric, spaces = false")

# Is all alphabetic
print(str(snumeric.isalpha()) + "<--- Checks if string is alphabetical, spaces = false")

#Is all numeric
print(str(snumeric.isnumeric()) + "<--- Checks if string is numeric, spaces = false")

#escape to add quotes
print('Today\'s day was the day\'s day')

print("""Lorem 
ipsum, 
dolor 
sit 
amet 
consectetur
 adipisicing 
 elit. Voluptates 
 voluptatum maiores
  quae ab asperiore
  s rerum error ita
  que optio? Asperio
  res veritatis sequ
  i corporis l
     earum, asperior
     es doloribus vo
     luptate. Dolore
     mque expedita s
     aepe incidunt c
     onsequuntur tem
     poribus beatae 
     iusto earum ex!
     """)


print("Nick " + "Computer")

print("Nick " * 27)
#You may not be able to add strings to integers, but you can multiply by them!
print(((60//7) * 700)%8 * "8") #the reason it outputs nothing is because the answer is 0
# print(((60**3)//8) * '\n2') #\n for new line

#If you want to add quotations without issues use escape character aka backslash \

print("I like \"Nick\" ")

print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

# step 1
beatles = []

print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Step 2:", beatles)

# step 3
for i in beatles:
    x = input("Add Stu Sutcliffe and Pete Best: ")
    if "Stu Sutcliffe" and "Pete Best" in beatles:
       break
    elif x == "Stu Sutcliffe":
        beatles.append("Stu Sutcliffe")
    elif x == "Pete Best":
        beatles.append("Pete Best")
        

print("Step 3:", beatles)

# step 4
print("Step 4:", beatles)
del beatles[3:]

# step 5
beatles.insert(0, "Ringo Starr")

print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
'''
Lists (and many other complex Python entities) are stored in different ways than ordinary (scalar) variables.

You could say that:

the name of an ordinary variable is the name of its content;
the name of a list is the name of a memory location where the list is stored.
'''
# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'

print(ord("a")) # used to find code point for character
print(ord("2"))

print(chr(21)) # used to find character based on code point
print(chr(61))

# min() is used to find the lowest code character 

print(min("Nick'shere"))

# max() is used to find the highers or maximum element of a sequence 

print(max("wadnoawjdoaszdfSADAWGA"))

