
# finding min_sum subarray using fixed size window + incremental


def min_sum(arr, k):
    if len(arr) < k:
        return 0
    
    cur_sum = sum(arr[:k])
    min_sum = cur_sum

    for i in range(k, len(arr)):
        cur_sum += arr[i]-arr[i-k]
        min_sum = min(cur_sum, min_sum)
    return min_sum


# using fixed sliding incremental 

def min_subarr(arr, k):
    if len(arr) < k:
        return []
    
    cur_sum  = sum(arr[:k])

    min_sum = cur_sum
    start_index = 0

    for i in range(k, len(arr)):
        cur_sum += arr[i] - arr[i-k]
        if cur_sum < min_sum:
            min_sum = cur_sum
            start_index = i - k + 1
    return arr[start_index:start_index + k]


# finding subarray itself

def min_sum_subarray(arr, k):
    if len(arr) < k:
        return []
    
    start = 0
    end = 0
    min_sum = float('inf')
    cur_sum = 0
    start_index = 0

    while end < len(arr):

        cur_sum += arr[end]

        if end-start+1 == k:
            min_sum = min(min_sum, cur_sum)
            start_index = start

            start += 1
        end += 1

    return arr[start_index:start_index+k]