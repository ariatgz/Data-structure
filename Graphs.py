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


class Node:

    def __init__(self, value):
        self.value = value
        self.adjecent_list = []
        self.visited = False


class Graph():

    def BFS(self,start):

        queue = Queue()
        queue.enqueue(start)
        start.visited= True


        traversal = []

        while len(queue) >0:

            actualNode= queue.dequeue()

            traversal.append(actualNode.value)

            for child in actualNode.adjecent_list:

                if child.visited is False:
                    queue.enqueue(child)
                    child.visited = True

        return traversal

    def dfs(self, start, traversal):



        start.visited = True
        traversal.append(start.value)

        for item in start.adjecent_list:
            if item.visited is False:
                self.dfs(item,traversal)

        return traversal









node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")

node1.adjecent_list.append(node2)
node1.adjecent_list.append(node3)
node1.adjecent_list.append(node4)
node3.adjecent_list.append(node1)
node2.adjecent_list.append(node5)
node2.adjecent_list.append(node1)
node2.adjecent_list.append(node6)
node4.adjecent_list.append(node7)


graph = Graph()
print(graph.dfs(node1,[]))