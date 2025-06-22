# using tail reursion


def count_digits(n, count = 0):

    if  n == 0:
        return count
    
    return count_digits(n // 10, count + 1)
print(count_digits(3456))