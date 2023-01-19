
def TwoSum(list, target):

    indexes={}

    for i in range(len(list)):

        if list[i] in indexes:
            return [indexes[list[i]], i]
        else:
            indexes[target - list[i]] = i








print(TwoSum([2,7,11,15],18))