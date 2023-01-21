class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None


class Solution:
    def reverseList(self, head):

        pre = None
        curr = head
        succ = None

        while curr != None:

            succ = curr.next
            curr.next = pre
            pre = curr
            curr = succ

        return pre




