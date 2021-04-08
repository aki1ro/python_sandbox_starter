# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
Functions vs. methods
A method is a specific kind of function - it behaves like a function and looks like a function, but differs in the way in which it acts, and in its invocation style.
'''
A function doesn't belong to any data - it gets data, it may create new data and it (generally) produces a result.

A method does all these things, but is also able to change the state of a selected entity.

A method is owned by the data it works for, while a function is owned by the whole code.

In general, a typical function invocation may look like this:

result = function(arg)


The function takes an argument, does something, and returns a result.



A typical method invocation usually looks like this:

result = data.method(arg)

Note: the name of the method is preceded by the name of the data which owns the method. Next, you add a dot, followed by the method name, and a pair of parenthesis enclosing the arguments.

The method will behave like a function, but can do something more - it can change the internal state of the data from which it has been invoked.
'''
#list function

print(len("Nick"))

nums = list(range(0, 30, 8))
print(len(nums))

nums = list(range(0,30))

nums2 = nums[2:18]

print(len(nums2))

print(len(nums[5:9]))

nums.append(list(range(34,64)))
print(nums)

nums.insert(0, 34)
print(nums)

nums.insert(13, 34)
words = ["Nick's here", "universe", "coding"]

words.insert(1, "Monkey's Banana")

words.append(1)
words.append("Hello there")
print(words)

print(words.index("coding"))

print(max(list(range(0, 55, 7))))

print(max([nums[3:10]]))

print(min(list(range(9,30, 5))))

print(nums.count(34))

nums.remove(34)

nums.reverse()

print(nums)

# string function
nums = [4, 5, 6, 7, 8, 9]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[4], nums[5])
print(msg)

print("This is Nums2:", nums2)
mynums = "My numbers: {0}, {1}, {1}, {3}, {4}".format(nums2[0], nums2[13], nums2[8], nums2[4], nums2[10])
#Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.
print(mynums)

stringformat = "{x}, {h}, {k}".format(x = 141%10, h = 6262//100, k = "Nick Here")

print(stringformat)

print("Nick is here, hallow world, and whatsup".split(" "))

print(mynums.split(" "))
mynums = mynums.split(" ")
mynums2 = "This is my numbers after a split \nwith formatting of randoms: {0} {1} {2} {3} {4}".format(mynums[3], mynums[1], mynums[4], mynums[1], mynums[0])

print(mynums2)

words2 = "These are some words to use for joining to a list,mmm yeeesss"
words3 = words2.join(mynums)
print(words3)

mynums3 = mynums2.join(mynums)

print("*****Crazy joining of the mynums1+2*****","\n", mynums3)
replace = "What Are These"
print(replace)
replace = replace.replace("What", "Apple")

replace = replace.replace("These", "What")

replace = replace.replace("Apple", "These")

print(replace)

print(mynums3.startswith("MyThis"))
print(mynums3.endswith("My12"))
print(mynums3.endswith(replace))

print(replace.lower())
print(replace.upper())

def my_func():
   print("spam")
   print(replace)
   print(mynums3)

my_func()


def calc_addition():
   x = int(input())
   y = int(input())
   print(x + y)


def add_exclamation(word):
   print(word + "!")

add_exclamation("What's good")
add_exclamation(str(input("Add word here:")))

def minus_one(minus):
   print(minus - 1 )

minus_one(1)
minus_one(141)


def equal(x, y):
   j = "EQUAL"
   z = "NOT EQUAL"
   if x == y:
      return j
   else:
         return z
         #return ends the function, and thus code placed after the return statement won't be executed
         
print(equal(1,3))

u = equal(4,4)

print(u)

# letter = ["day day day", "end end end", "day", "end"]
# x = str(input())
# print(letter.count(x))
# print(x.count(x))

text = input("Enter Text for count:")
letter = input("Letter to Search for:")


def letter_count(text, letter):
   count = 0
   for x in text:
      if x == letter:
         count += 1
         continue
   else:
      return count

print(letter_count(text, letter))

def letter_count1(text, letter):
   count = 0
   for x in text:
      count += (x == letter)
   else:
      return count
   
        

print(letter_count1(text, letter))
                  
"""
comment known as a docstring

"""


text = input("Text here:")
word = input("word here:")

list = text.split(" ")
print(list)
def search(text,word):
    for x in list:
       if x == word:
          return "Word found"
    else:
       return "Word not found"
        


print(search(text, word))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


def percentage(n, k):
   p = k /100 * n
   print(p)


n = int(input())
k = int(input())

percentage(n, k)