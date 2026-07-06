class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            self.minStack.append(self.stack.pop())
        
        while len(self.minStack):
            self.stack.append(self.minStack.pop())
        
        return mini
