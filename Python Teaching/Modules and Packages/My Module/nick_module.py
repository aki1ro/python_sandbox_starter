print("This is my module!")
print(__name__)

# When a file is imported its __name__ variable is set to the file's name ie module.py
# When a file is run directly, its __name__ variable is set to __main__.
__count = 0 # <--- Used to check how many times a function has been envoked, used as a counter to initiliaze to zero. 
if __name__ == '__main__': # <--- checks to see if __name__ is = __main__ 
   #prevent your module's user from running your code as an ordinary script.
   print("I prefer to be a module")
else:
   print("I like to be a module")

