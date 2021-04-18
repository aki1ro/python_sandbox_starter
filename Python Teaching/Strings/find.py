'''
The find() method is similar to index(), which you already know - it looks for a substring and returns the index of first occurrence of this substring, but:

it's safer - it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
it works with strings only - don't try to apply it to any other sequence.
'''

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')

while fnd != -1:
   print(fnd)
   fnd = the_text.find("the", fnd + 1)


print("Nick was here so don't worry".find('a', 1, 20))



