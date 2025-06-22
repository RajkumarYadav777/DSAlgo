
# using while loop we can count number of 0s

def count_zeros(n):
    
    count = 0
    
    while n > 0:
        digit = n % 10

        if digit == 0:
            count += 1

        n //= 10
    return count
print(count_zeros(10200))