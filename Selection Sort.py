def SelectionSort(arr):


    for i in range(len(arr)):
        smallest = i

        for j in range(i+1, len(arr)):

            if arr[j] < arr[smallest]:
                smallest= j

        arr[i],arr[smallest] = arr[smallest],arr[i]



arr = [20, 12, 10, 12, 2]

SelectionSort(arr)

print(arr)
