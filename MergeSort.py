def MergeSort(my_array):
    if len(my_array) == 1:
        return my_array

    middle=len(my_array) // 2
    left= my_array[0:middle]
    right=my_array[middle:len(my_array)]

    left_result= MergeSort(left)
    right_result= MergeSort(right)

    return Mergerer(left_result, right_result)


def Mergerer(left,right):

    tempList=[None] * (len(left)+len(right))

    i=0
    j=0
    k=0

    while i<len(left) and j<len(right) :
        if left[i] <= right[j]:
            tempList[k] = left[i]
            i += 1

        else:
            tempList[k] = right[j]
            j += 1
        k+=1

    while i < len(left):
        tempList[k] = left[i]
        i += 1
        k+=1

    while j < len(right):
        tempList[k] = right[j]
        j += 1
        k += 1


    return tempList



print(MergeSort([4, 5, 6, 1, 3, 7, 2]))
