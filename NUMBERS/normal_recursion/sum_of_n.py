

# here we use normal recursion that means,
#  we just pass the result down to its parent until it reaches the main call


def sum_n(n):
    if n == 0:
        return 0
    
    return n + sum_n(n-1)
print(sum_n(10))