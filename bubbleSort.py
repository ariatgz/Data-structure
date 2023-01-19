
def bubbleSort(arr):

    my_range= len(arr ) -1

    for i in range(my_range):
        for j in range(my_range -i):
            if arr[j] > arr[ j +1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp




arr = [29, 10, 14, 37, 15 ,-9 ,-3]
bubbleSort(arr)

print(arr)
