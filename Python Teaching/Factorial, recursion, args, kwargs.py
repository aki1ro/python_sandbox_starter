def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

print(factorial(5))

#For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!.


def fac(x):
   if x % 2 == 0:
      return 0
   else:
      return x * factorial(x-1)

print(fac(5))


def is_greater_than_ten(x):
   if x > 10:
      return "Is greater than 10"
   else:
      return is_less_than_ten(x)

def is_less_than_ten(x):
   if x < 10:
      return "Is less than 10"
   else:
      return is_greater_than_ten(x)

def is_equal_to_10(x):
   if x == 10:
      return "Is equal to 10"
   elif x > 10:
      return is_greater_than_ten(x)
   elif x < 10:
      return is_less_than_ten(x)



print(is_greater_than_ten(13))
print(is_less_than_ten(12))

print(is_equal_to_10(10))



def convert(num):
   if (num == 0):
      return num
   else:
      convert(num//2)
      print(num%2,end="") #end="" is used to print all on the same line.

 
      
      

   

convert(int(input()))


def func(x, *home): #*args are returned as tuples. doesn't have to be "*args" can be "*anything"
   while x < 10:
      x += 1
      print(x, end="")
      if x == 10:
         print(home)

func(1,"Nick's args are printing")
#**kwargs return as a dictoinary, are used to make statements on variables not yet defined
def func2(x, *args,**kwargs):
   print(x, args, kwargs)

func2(5, 2131, a=6) # a = 6 being the keyword argument.
#The arguments returned by **kwargs are not included in *args


#printing none also known as null
def my_min1(*nums):
    for n in nums:
        b = n
        if b > n:
            return n
        else:
            continue



print(my_min1(8, 13, 4, 42, 120, 7))

def args(*nums):
    print(nums[:2])

args(4, 5, 6, 7, 8, 9, 20, 30, 42)

def my_min(*nums):
   b = nums[0]
   for i in nums[1:]:
      if i < b:
         b = i
   else:
       return b



print(my_min(8, 13, 4, 42, 120, 7))


# Python3 code for decimal to binary
# conversion using recursion
  
# Decimal to binary conversion 
# using recursion
def getbinary(number):
   
    # Base case
    if number == 0:
        return 0
       
     # Recursion call and storing the result
    smallans = getbinary(number // 2)
     
    return number % 2 + 10 * smallans
   
# Driver Code
decimal_number = 1048576
print(getbinary(decimal_number))
  
# This code is contributed
# by "Sarthak Sethi"


