'''
In Python, a statement is typically a line of code we write to give an “instruction” or “command” for Python to perform. For example, variable assignment, which we used quite often, is a statement, which tells Python to set a variable to a value, which it carry out when it processes that code line. Statements are essentially always an “imperative” task that must be carried out.

On the other hand, functions are a collection of multiple code lines which you are able to call all at once. Functions themselves are not statements, because they are not an imperative task that must be performed. Rather, they are closer to some object or value, that you can call in your program when you need to run its code.

In addition, statements do not return anything, while functions always return some value, returning the value None if no return value is specified.
'''

#Example of a statement:
x = 9 
y = 6

sum = x + y

#all statements as they are instructions or commands to perform. In this case we are telling python to set x as 9 and y as 6, also sum as x + y. 

#Example of a function:

print(sum)

#This is a function as it's essentially a set of instructons you can call all at once. The function itself isn't a statement, as it's not an imperative task that it must perform meaning it doesn't have to go through a set of code to do it's task. As it can run the whole set of code required merely by calling this one function. 
 

