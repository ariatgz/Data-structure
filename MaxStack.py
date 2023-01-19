class MaxStack:

    def __init__(self):

        self.maxVals= []
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.maxVals) == 0:
            self.maxVals.append(val)

        elif val >= self.maxVals[-1]:
            self.maxVals.append(val)


    def pop(self) -> None:
        value =self.stack.pop()

        if value == self.maxVals[-1]:
            self.maxVals.pop()


        return value

    def top(self) -> int:
        return  self.stack[-1]

    def getMax(self) -> int:


        return self.maxVals[-1]


obj = MaxStack()
obj.push(2)
obj.push(3)
obj.push(0)
obj.push(11)
obj.push(8)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMax()
print(param_4)