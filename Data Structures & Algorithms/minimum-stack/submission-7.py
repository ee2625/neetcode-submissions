class MinStack:

    def __init__(self):
        self.nums = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.nums.append(val)
        if not self.MinStack:
            self.MinStack.append(val)
        elif val <= self.MinStack[-1]:
            self.MinStack.append(val)

    def pop(self) -> None:
        num = self.nums.pop()
        if num == self.MinStack[-1]:
            self.MinStack.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
