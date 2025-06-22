# after every iteration one element is pushed to end of the array
# len(arr)-i-1 ; thats why we no need to compare end of the arr ,because we get sorted for every itertion


def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [3,5,8,9,1,5,2]
print(bubblesort(arr))