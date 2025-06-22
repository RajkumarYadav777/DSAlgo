
# here we use normal recursion to find factorial of a number

def fact(n):
    if n == 0 or n == 1:
        return 1
    
    return n * fact(n-1)

print(fact(5))

# we can use lambda

fact = lambda n : 1 if n == 0 else n * fact(n-1)
print(fact(5))