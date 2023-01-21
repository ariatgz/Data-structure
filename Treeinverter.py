class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def TreeInverter(root):

    if root is None:
        return

    root.right,root.left= root.left,root.right

    TreeInverter(root.left)
    TreeInverter(root.right)
