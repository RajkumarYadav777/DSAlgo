# in this sorting appproach we find spot and insert in its place
# assumes first element is in sorted position and then compae and insert 
# Find the correct position to 
# insert the current key (element) within the already sorted left part of the array.

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr