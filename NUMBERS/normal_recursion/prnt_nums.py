

# for printing numbers here we use recursion 
# in this approach top-down , process before the recursive call

def r_prnt_nums(n, i):

    # base case
    if n < i:
        return 
    print(i)
    r_prnt_nums(n, i + 1)
r_prnt_nums(10, 0)

# bottom-up approach
# here after all recursion, process will start

def prnt_nums_r(n , i):
    if n < i:
        return
    
    prnt_nums_r(n, i+1)
    print(i)   # printing reverse order

prnt_nums_r(10, 0)