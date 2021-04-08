#type of iterable, like lists or tuples

# can be iterated through with "for" loops, doesn't allow indexing with arbitrary indices

# the "yield" statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables


def counter_to_100():
   i = 0
   while i <= 100:
      yield i
      i += 1

for i in counter_to_100():
   print(i) 

x = int(input("Insert number:"))
#In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

def infinite_number(x):
   while True:
      yield x

for i in infinite_number(x):
   print(i)

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(f, t):
    r = range(f, t)
    for x in r:
        if isPrime(x) == True:
            yield x
            

f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))

          