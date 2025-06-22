# here we use while loop 

def sum_digit(n):
    sum = 0

    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum
print(sum_digit(3456))