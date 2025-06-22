
# normal recursion

def normal_count_zero(n):
    if  n == 0:
        return 0
    
    digit = n % 10

    if digit == 0:
        return 1 + normal_count_zero(n // 10)
    return normal_count_zero(n//10)
print(normal_count_zero(10200))


# here if user enters n=0 count is 1
# but eventually we make n as zero to stop recursion so here count 0
# we can use helper

def count_zero(n):
    if n == 0:
        return 1
    
    def helper(n):
        if n == 0:
            return 0
        
        digit = n % 10
        return (1 if digit == 0 else 0) + helper(n // 10)
    return helper(n)
print(count_zero(102030))