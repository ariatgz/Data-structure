class MinStack:

    def __init__(self):

        self.minVals= []
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minVals) == 0:
            self.minVals.append(val)

        elif val <= self.minVals[-1]:
            self.minVals.append(val)


    def pop(self) -> None:
        value =self.stack.pop()

        if value == self.minVals[-1]:
            self.minVals.pop()


        return value

    def top(self) -> int:
        return  self.stack[-1]

    def getMin(self) -> int:


        return self.minVals[-1]


obj = MinStack()
obj.push(-2)
obj.push(-3)
obj.push(0)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)