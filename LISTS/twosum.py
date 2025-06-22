# here we need to return two indices that adds up to target

# we will use classic hashmap technique
# in dict we use num as keys and id as value


def twosum_hashmap(nums, target):
    num_map = {}

    for  id, num in enumerate(nums):
        complement = target-num
        if complement in num_map:
            return num_map[complement], id
        num_map[num] = id
    return 'no valid indices found'
print(twosum_hashmap([1,3,5,2,4,9,5,6], 7))

# basic two pointers technique
# in this approach array must be sorted

def two_sum_twopointers(arr, target):
    # here we must preserve their original indexs

    original = [(val, id) for id, val in enumerate(arr)]

    # sort by value [(val, id)]
    original.sort(key=lambda x :x[0])
    left = 0
    right = len(original)-1

    while left < right:
        total = original[left][0] + original[right][0]
        if total == target:
            return original[left][1], original[right][1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return 'no indices found'

# pointers movement
''' elif total < target:
         left += 1
    else:
        right -= 1
  
Means: the sum is too small, so you need a bigger number.

Since the array is sorted, the only way to get a bigger number 
is to move left pointer to the right:
'''



