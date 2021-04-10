# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#Each element in a dictionary is represented by a key:value pair.

# # Simple dict
# person = {
#       "first_name": "Josh",
#       "last_name": "Forster",
#       "age": "27",
#       "height": "1.85m",
#       "weight": "75kg"

# }

# print(person) 

# numbers = {
#       "Cell": "805-525-4141",
#       "Home": "805-518-7261",
#       "Emergency": 911
# }

# print(numbers)

# print(len(person))

# #Only immutable objects can be used as keys to dictionaries. Immutable objects are those that can't be changed.
# #This means that you can use strings, integers, booleans, and any other immutable type as dictionary keys.

# data = {
#     'Singapore': 1,
#     'Ireland': 6,
#     'United Kingdom': 7,
#     'Germany': 27,
#     'Armenia': 34,
#     'United States': 17,
#     'Canada': 9,
#     'Italy': 74
# }


# country = input()

# print(data.get(country, "Not found"))


# for x in data:
#       print(x)




text = list(input())
dict = {}
#your code goes here



for n in text:
    c = 0
    if n in text:
          c = text.count(n)
          dict.update({n:c})
print(dict)




