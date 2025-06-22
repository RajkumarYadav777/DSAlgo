# here we use while loop to reversing digit

def reverse_digit(n):
    rev = 0

    while n > 0:
        r = n % 10
        rev = r + rev*10
        n //= 10
    return rev
print(reverse_digit(3456))