
# here we use while loop for printing sum of n natural numbers

def sum_n(n):
    sum = 0

    while n:
        sum += n
        n -= 1
    return sum
print(sum_n(10))