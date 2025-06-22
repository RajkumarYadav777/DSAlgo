
# here we use tail recursion that means it just calculates the res at the time of 
# recursion only
# tail recursions mostly contain result paramter, it will be returned when done from base case

def sum_of_n(n, sum):

    if n == 0:
        return sum
    
    return sum_of_n(n-1, sum + n)

print(sum_of_n(10, 0))


# another version

def n_sum(n, sum=0):

    if n == 0:
        return sum
    
    sum += n
    return n_sum(n-1, sum)
print(n_sum(10))