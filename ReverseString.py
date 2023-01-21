def reverser(list):

    right = 0
    left= len(list) - 1

    while left > right:


        list[right], list[left]= list[left], list[right]

        right += 1
        left -=1






list = ["H","a","n","n","a","h"]

s = ["h","e","l","l","o"]



print(reverser(list))




