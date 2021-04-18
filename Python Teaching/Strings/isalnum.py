'''
The isalnum() method
The parameterless method named isalnum() checks if the string contains only digits or
alphabetical characters (letters), and returns True or False according to the result.
'''

print("nick was kind of here but not really 4141".isalnum())
# Note: any string element that is not a digit or a letter causes the method to return
# False. An empty string does, too.
print("nick was kind of here but not really".isspace())

print("nickwaskindofherebutnoreally3241".isalnum())

print("nickwashere".isalnum())

print("nick".isalpha())

print("14141".isdigit())

# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

