# max_sum using fixed sliding with incremental

def max_sum(arr, k):
    if len(arr) < k:
        return 0
    
    cur_sum = sum(arr[:k])
    max_sum = cur_sum

    for i in range(k, len(arr)):
        cur_sum -= arr[i-k]
        cur_sum += arr[i]
        max_sum= max(max_sum,cur_sum)
    
    return max_sum


# two pointers approach

def max_sum_two_pointers(arr, k):
    if len(arr) < k:
        return 0
    
    start = 0
    end = 0
    cur_sum = 0
    max_sum = 0

    while end < len(arr):
        cur_sum += arr[end]

        if end-start+1 == k:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= arr[start]
            start += 1
        end += 1
    return max_sum

# finding the subarray

def max_sum_subarray(arr,k):
    if len(arr) < k:
        return []
    
    cur_sum = sum(arr[:k])
    max_sum = cur_sum
    start_index = 0

    for i in range(k, len(arr)):
        cur_sum += arr[i] - arr[i-k]
        if cur_sum > max_sum:
            max_sum = cur_sum
            start_index = i-k+1
    return arr[start_index:start_index+k]
            