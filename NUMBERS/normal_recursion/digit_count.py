

# using normal recursion'

def count_digits(n) : 
    if n == 0:
        return 1
    def helper(n):
        if n == 0 :
            return 0 
        
        return 1 + helper(n // 10)
    return helper(n)
print(count_digits(3456))