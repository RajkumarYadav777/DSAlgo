
# we use tail recursion to find a factorial of a number

def fact_tail(n, fact = 1):

    if n == 0 or n == 1:
        return fact
    
    return fact_tail(n-1, fact * n)
print(fact_tail(5))