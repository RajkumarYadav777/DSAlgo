# to find the missing number 0 - n
# we have mathematical fomuna n*(n+1)//2
# total sum - actualsum gives us missing number

def find_missing_num(arr):
    n = len(arr)

    total_sum = n*(n+1)//2
    actual_sum = sum(arr)
    return total_sum-actual_sum
print(find_missing_num([0,1,2,3,4,6,7,8,9]))

# if question to find missing number from 1 to n 
# n = len(arr) + 1

# 0 to n -> it includes 0 so n+1
# one number is missing -> n+1-1= n (len(arr))

# 1 to n -> 0 is not inclusing so -> n
# one number is missing -> n-1
# to get actual n we add +1 -> n+1-> len(arr) +1
