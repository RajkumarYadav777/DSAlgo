# here we find digit sum with out convertng number to string

def digit_sum(n):
    if n <= 0:
        return 'number must be greater than 0'
    if n == 1:
        return 1
    
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum
