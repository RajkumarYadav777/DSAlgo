# ITERATIVE APPROACH
# in binary search array must be sorted

def bin_search(arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            low = mid+1
        else:
            high = mid-1
arr = [1,2,3,4,5,6,7]
target = 5
print(bin_search(arr,target))



# RECURSIVE VERSION
def binary_search(arr, target):
    def helper(low, high):
        if low > high:
            return -1
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            return helper(mid+1, high)
        else:
            return helper(low, mid-1)
    return helper(0, len(arr)-1)
print(binary_search(arr, target))