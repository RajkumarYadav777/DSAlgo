
# count subarray of size k, with avg >= target

def count_sum_avg(arr, k, target):

    if len(arr) < k:
        return 0
    
    cur_sum = sum(arr[:k])
    count = 0
    avg = cur_sum/k
    if avg >= target:
        count += 1
    
    for i in range(k, len(arr)):
        cur_sum += arr[i] - arr[i-k]
        avg = cur_sum/k

        if avg >= target:
            count += 1
    return count



# using two pointers approach(manually build window)


def count_avg_target(arr, k, target):
    if len(arr) < k:
        return 0
    
    start = 0
    end = 0
    count = 0
    cur_sum = 0

    while end < len(arr):
        cur_sum += arr[end]

        if end - start + 1 == k:
            avg = cur_sum/k

            if avg >= target:
                count += 1
            
            cur_sum -= arr[start]
            start += 1
        end += 1

    return count



