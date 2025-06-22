

# here we use tail recursion using accumalator

def count_zero_tail(n):
    if n == 0:
        return 0
    
    def helper(n, count):
        if n == 0:
            return count
        digit = n % 10

        return helper(n // 10, count + 1) if digit else helper(n // 10, count)
    return helper(n , 0)
print(count_zero_tail(1020))
