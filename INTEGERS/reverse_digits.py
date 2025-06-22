# to reverse numbers

def rev_digits(n):
    if n <= 0:
        return 'number must be greater than 0'
    
    rev = 0

    while  n > 0:
        dig = n % 10
        rev = dig + rev*10
        n //= 10
    return rev
print(rev_digits(34567))