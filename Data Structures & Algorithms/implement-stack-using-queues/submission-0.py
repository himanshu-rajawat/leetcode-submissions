class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        size = len(self.q)
        res = None
        for i in range(size-1):
            res = self.q.pop()
            self.q.append(res)
        res = self.q.pop()
        return res

    def top(self) -> int:
        size = len(self.q)
        res = None
        for i in range(size):
            res = self.q.pop()
            self.q.append(res)
        return res
        

    def empty(self) -> bool:
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()