# here we use tail recursion

def sum_digits(n, sum = 0 ):

    if n == 0:
        return sum
    digit = n % 10
    return sum_digits(n //10, sum + digit)

print(sum_digits(3456))
