# here we count digits

def digit_count(n):
    if n <= 0:
        return ' number must be greater than 0'
    if n == 0 or  n == 1:
        return 1
    
    count = 0

    while n > 0:
        dig = n % 10
        count += 1
        n //= 10
    return count
print(digit_count(234567))