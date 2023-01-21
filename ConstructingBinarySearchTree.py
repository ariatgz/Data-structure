class TreeNode:

    def __init__(self, val):
        self.value = val
        self.right= None
        self.left = None


class Soloution:
    def bstFromPreorder(self,preorder):

        root = TreeNode(preorder[0])

        stack = [root]

        for i in range(1,len(preorder)):

            if preorder[i] < stack[-1].value:
                node = TreeNode(preorder[i])
                stack[-1].left = node
                stack.append(node)
            else:
                poped = None
                while stack and stack[-1].value < preorder[i]:
                    poped = stack.pop()

                node = TreeNode(preorder[i])
                poped.right = node
                stack.append(node)





