
# using while loop we find factorial of a number

def fact(n):

    if n == 0 or n == 1:
        return 1
    
    prod = 1

    while n > 0:
        prod *= n
        n -= 1
    
    return prod

print(fact(5))