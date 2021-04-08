# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]

#Using a constructor (to build the list)
numbers2 = list((1, 2, 3, 4, 5, 6))

print(numbers)

print(numbers2)

# Printing indexed strings

fruits = ["Apples", "Oranges", "grapes", "Pears"]

#Get value
print(fruits[0])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

print(fruits)
print(fruits[4])

# Remove from list
fruits.remove('Oranges')
fruits.remove('grapes')
print(fruits)

# Insert into position
fruits.insert(0, "Blueberries")
print(fruits)

# Remove from position Note: passing null removes last
fruits.pop(1)
print(fruits)

# Reverse the list
fruits.reverse()
print(fruits)

#Sorting list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)


things = [1, 2, 3, "thing 1", "thing 2",fruits]

print(things)

print(things[4])

m = [
[1, 2, 3],
[7, 8, 9]
]

print(m[1][2])

print(m[0][2])

print((m[0][2]) + (m[1][1]))

string = "Hello String!"

print(string[12])

print(string[11])

x = [2, 3]

x += [3, 4]

print(x)

# fname = input()
# lname = input()

# print(fname[0] + lname[0])

# name = input()

# name += input()

# print(name[0] + '.' + name[5] + '.')


# commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]
# # your code goes here
# # x = input()
# if x not in commands:
#    print("Not supported")
# else:
#    print("OK")

# commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]
# # your code goes here
# # x = input()
# if x not in commands:
#    print("OK")
# else:
#    print("Not supported")



# # x = input()

# if x == "Lights Off":
#    print("OK")
# elif x == "Lock the door":
#    print("OK")
# elif x == "Open the door":
#    print("OK")
# elif x == "Make Coffee":
#    print("OK")
# elif x == "Shut down":
#    print("OK")
# else:
#    print("Not supported")

# #List comprehension

cube = ["for" for i in range(20)]

print(cube, "<------range cube")

word = input()

#word without vowels

letters = list(word)

novowelword = []

vowel = ['a', 'e', 'i', 'o', 'u']

for letter in letters:
    if letter in vowel:
        novowel=True
    elif letter not in vowel:
        novowel=False
        novowelword.append(letter)
print(novowelword)

word = input()

letters = list(word)

novowelword = []

vowel = ['a', 'e', 'i', 'o', 'u']

for x in letters:
    if x not in vowel:
        novowelword.append(x)
print(novowelword)

word = input()

letters = list(word)

novowelword = []

vowel = ['a', 'e', 'i', 'o', 'u']

for x in letters:
    if x in vowel:
        letters.remove(x)
print(letters)


def my_func(f, arg):
  return f(arg)
  u = input(int())
  my_func = my_func(lambda x: 2*x*x,arg) 
  print(my_func)



salaries = [2000, 1800, 3100, 4400, 1500]

bonus = int(input())


new_salary = list(map(lambda x: x + bonus, salaries))


print(new_salary)