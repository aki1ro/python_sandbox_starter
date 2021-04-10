# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are very similar to lists, except that they are immutable (they cannot be changed).
 
# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')

#Using Construtor
fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

#Get single value
print(fruit_tuple[1])


# Can not change value
#fruit_tuple[1] = 'Grape'

# Tuple with one value should have trailing command
fruit_tuple_2 = ('Apple',)

print(fruit_tuple_2)

# Get length of tuple 
print(len(fruit_tuple))


# A Set is a collection which is unordered and unindexed. No duplicate members.
fruit_set = {'Apple', 'Orange', 'Mango'}

print(fruit_set)

# Check if in set
print('Apple' in fruit_set)

#Add to set
fruit_set.add('Grape')

print(fruit_set)

# Clear set
fruit_set.clear()

print(fruit_set)

# Delete a set
del fruit_set


#Tuples
numbers = ("805-414-111", "944-214-2431", "234-414-8121")

animals = ("Gorrila", "Banana", "Bunny", "Fox", "Goat")

print(type(numbers))

print(animals[2:5])






contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]





print(contacts[0])

#once you unpack a tuple, you can change it
numbers = (1, 2, 3)
h, bill, what_whhat = numbers
print(h)
print(bill)
print(what_whhat)

what_whhat = 0

print(what_whhat)

# * in front of value will take remainder of tuple into that value
power_rangers = "Red", "Blue", "Green", "Purple", "Black"

ranger1, ranger2, *ranger3, ranger4 = power_rangers

print(ranger1)
print(ranger2)
print(ranger3)
print(ranger4)

ranger1 = "Yellow"

ranger3 = ["Silver", "Gold", "White"]

print(ranger1)
print(ranger3)
print(ranger2, ranger3, ranger1, ranger4)
side = int(input())

def calc(x):
   p = side + side + side + side
   print("Perimeter:",p)
   a = side**2
   print("Area:",a)
   
calc(side)
'''
set Sets are similar to lists or dictionaries.
They are created using curly braces, and are unordered, which means that they can't be indexed.

Due to the way they're stored, it's faster to check whether an item is part of a set using the in operator, rather than part of a list.
'''

num_set = {1, 2, 3, 4, 5, 2}

print(num_set)

print(3 in num_set)

num_set.remove(3)

num_set.add(6)

print(num_set)

print(len(num_set))

'''
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.
'''
print("\n")

set = {3, 4, 5, 6, 7, 8, 9}

set2 = {4,3,2,5,10,14,51}


print(set | set2)
print(set & set2)
print(set - set2)
print(set2 - set)
print(set ^ set2)


skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

a, = skills & job_skills
print(a)




nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)

print(nums)