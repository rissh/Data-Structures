
class MyQueue:

    def __init__(self):
        self.write = []
        self.read = []
        

    def push(self, x: int) -> None:
        self.write.append(x)

    def pop(self) -> int:
        if self.write == []:
            return None

        while self.write != []:
            self.read.append(self.write.pop())

        res = self.read.pop()
        while self.read != []:
            self.write.append(self.read.pop())

        return res            

    def peek(self) -> int:
        
        if self.write == []:
            return None

        else:
            return self.write[0]

    def empty(self) -> bool:
        return self.write == []        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
