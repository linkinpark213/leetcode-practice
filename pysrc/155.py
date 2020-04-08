class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.min = []

    def push(self, x: int) -> None:
        self.list.append(x)
        self.min.append(x if len(self.min) == 0 or x < self.min[-1] else self.min[-1])

    def pop(self) -> None:
        self.min.pop()
        return self.list.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min[-1]


if __name__ == '__main__':
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
