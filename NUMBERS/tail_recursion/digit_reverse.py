# here we use tail recursion

def rever_digits(n, rev = 0):
    if n == 0 :
        return rev
    
    r = n % 10

    return rever_digits(n // 10, r + rev * 10)
print(rever_digits(3456))