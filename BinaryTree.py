class Node():

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Queue():

    def __init__(self):
        self.array=[]

    def enqueue(self,value):
        self.array.append(value)

    def dequeue(self):
        if len(self.array):
            return self.array.pop(0)

    def peek(self):
        if len(self.array):
            return self.array[0].value

    def __len__(self):
        return len(self.array)




class Binarytree():

    def __init__(self, value):
        self.root = Node(value)

    def preorder(self, start, traversal):
        # root -> left -> Right
        if start is None:
            return
        # changing the order of the next three operation changes the DFS' order.
        traversal.append(start.value)

        self.preorder(start.left, traversal)

        self.preorder(start.right, traversal)

        return

    def levelorder(self, start):

        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = []

        while len(queue) > 0:
            traversal.append(queue.peek())

            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)


        return traversal






tree = Binarytree(3)

tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(tree.levelorder(tree.root))
