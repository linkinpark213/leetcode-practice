class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.m = []

    def push(self, x: int) -> None:
        self.l.append(x)
        if len(self.m) == 0 or x < self.m[-1]:
            self.m.append(x)
        else:
            self.m.append(self.m[-1])

    def pop(self) -> None:
        self.m.pop()
        return self.l.pop()

    def top(self) -> int:
        return self.l[-1]

    def min(self) -> int:
        return self.m[-1]

if __name__ == '__main__':
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.min())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.min())
