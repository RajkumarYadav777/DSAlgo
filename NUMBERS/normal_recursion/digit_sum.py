
# here we use normal recursion

def sum_of_digits(n):
    if n == 0:
        return 0
    
    digit = n % 10

    return digit + sum_of_digits(n // 10)
# or simply return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(3456))