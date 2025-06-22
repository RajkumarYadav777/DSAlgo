# to count zeros 

def cnt_zeros_str(n):
    count = 0

    for dig in str(n):
        if int(dig) == 0:
            count += 1
    return count
print(cnt_zeros_str(1020300))

# using while without converting string

def count_zeros(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        last_dig = n % 10
        if last_dig == 0:
            count += 1
        n = n//10
    return count
print(count_zeros(1020300))

# n%10 gives last digit
# n = n//10 updates n by removing last digit eventually it makes n as 0

