class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))
        temp = self.q1[0]
        self.q1 = self.q2
        del self.q2
        self.q2 = []
        return temp

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


if __name__ == '__main__':
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.q1)
    param_2 = obj.pop()
    print(obj.q1)
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)
