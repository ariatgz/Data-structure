def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    result = helper(array, target, left, right)
    return result


def helper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    middle_elem = array[middle]

    if target == middle_elem:
        return middle

    elif middle_elem > target:
        return helper(array, target, left, middle - 1)

    else:
        return helper(array, target, middle + 1, right)




print(binarySearch([1, 2, 3, 4, 5, 6], 2))
