def checkPalindrome(st, left, right):

    while left >= 0 and right< len(st) and st[left]==st[right]:
        left -= 1
        right += 1

    return st[left+1:right]

def longestPalindrome(s):

    result=""

    for i in range(len(s)):

        word1 = checkPalindrome(s, i, i)
        word2= checkPalindrome(s, i, i+1)

        if len(word1)>= len(word2):
            longest=word1
        else:
            longest=word2

        if len(longest) >= len(result):
            result= longest
        else:
            result=result

    return result




print(longestPalindrome("a"))
