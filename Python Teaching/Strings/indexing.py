# indexing strings

string = "Nick's walking silly"

for i in range(len(string)):
   print(string[i], end =' ') # end = adds a whitespace inbetween the letters.

print() # used to print a new line to seperate strings

for i in string:
   print(i, end =' ')

print()


# index() method is used to search a sequence from beginning, in order to find the first 
# element of the value specified in its argument

print("nickwashere214100WQ@$!%!".index("h"))

