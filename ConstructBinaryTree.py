class Node:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


class Soloution:
    def buildTree(self, preorder, inorder):

        if len(preorder) == 1:

            return Node(preorder[0])

        if len(inorder) == 0:
            return


        index_root = inorder.index(preorder.pop(0))

        node = Node(inorder[index_root])

        node.left = self.buildTree(preorder, inorder[:index_root])

        node.right = self.buildTree(preorder, inorder[index_root + 1:])

        return node