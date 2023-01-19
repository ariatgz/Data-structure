def QuickSort(arr):
    QuickHelper(arr, 0, len(arr)-1)
    return arr

def QuickHelper(arr, starting, length):
    if starting >= length:
        return

    pivot= starting
    left=starting+1
    right=length

    while right >= left:

        if arr[left] > arr[pivot] > arr[right]:
            arr[right],arr[left] = arr[left],arr[right]

        if arr[left] <= arr[pivot]:
            left+=1

        if arr[right] >= arr[pivot]:
            right -= 1

    arr[pivot], arr[right] = arr[right], arr[pivot]

    QuickHelper(arr, starting, right - 1)
    QuickHelper(arr, starting, right + 1)


array= [2,4,1,77,56]
print(QuickSort(array))

