# for merge sort we use divide and conquer approach

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
    
def merge(left, right):
    result = []
    i= 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j += 1
    # left overs
    result += left[i:]
    result += right[j:]
    return result
    
arr = [2,15,8,3,5,9,4]
print(merge_sort(arr))