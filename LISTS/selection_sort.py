# in selection sort , we choose first elements index as min index and rest of the
# elements are compared and if find min_id  we will updae and swap
# in-place comparision based algo


def selecion_sort(arr):
    for i in range(len(arr)):
        min_id = i
        
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_id]:
                min_id = j
        arr[i],arr[min_id] = arr[min_id], arr[i]
    return arr
print(selecion_sort([3,8,1,4,7,2,6]))