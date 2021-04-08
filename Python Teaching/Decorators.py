'''
Decorators provide a way to modify functions using other functions.

@(name of decorator func), Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.

If we are defining a function we can "decorate" it with the @ symbol

if you don't define a wrap below decorater it will run the functions below.

'''

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text(nm):
    print("Hello world!" +nm)

# print_text(input())

def decor2(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor2
def print_text2():
    print("Hello world!")



