def memoize(func):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(50))

var = '''nick is here
here is nick'''

print(var)