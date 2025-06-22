# here we use normal recursion
# in normal recursion we need to find digits positions to reverse


def rev_digits(n):
    # if n is single digit reverse is samw
    if n < 10:
        return n
    
    digits = len(str(n))
    return n%10 * (10 ** (digits-1)) + rev_digits(n // 10)
print(rev_digits(3456))


# using helper

def rev_digits_normal(n):
    if n == 0:
        return 0
    
    def helper(n, digits):
        if n == 0:
            return 0
        
        digit = n % 10
        return digit * (10 ** (digits-1)) + helper(n // 10, digits - 1)
    return helper(n, len(str(n)))
print(rev_digits_normal(3456))


# without helper

def rev_digit(n, digits = None):
    if digits is None:
        digits = len(str(n))
    
    if n == 0:
        return 0
    
    r = n % 10

    return r * (10 ** (digits-1)) + rev_digit(n // 10)
print(rev_digit(3456))
