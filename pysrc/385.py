class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.value = value
        self.list = []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return type(self.value) is int

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.list.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.value

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.list

    def __str__(self):
        if self.isInteger() or type(self.value) is str:
            return str(self.value)
        s = '['
        for i, v in enumerate(self.list):
            s += str(v)
            if i != len(self.list) - 1:
                s += ','
        s += ']'
        return s


class HonestSolution:
    def deserialize(self, s: str) -> NestedInteger:
        val = 0
        ptr = NestedInteger()
        stack = [ptr]
        isNum = False
        sign = 1
        for c in s:
            if c >= '0' and c <= '9':
                val = val * 10 + int(c)
                isNum = True
            else:
                if c == '[':
                    newList = NestedInteger()
                    ptr.add(newList)
                    stack.append(newList)
                    ptr = newList
                    isNum = False
                    val = 0
                elif c == ']':
                    if isNum:
                        obj = NestedInteger()
                        obj.setInteger(val * sign)
                        ptr.add(obj)
                        sign = 1
                        isNum = False
                        val = 0
                    stack.pop()
                    ptr = stack[-1]
                elif c == ',':
                    if isNum:
                        obj = NestedInteger()
                        obj.setInteger(val * sign)
                        ptr.add(obj)
                        sign = 1
                        isNum = False
                        val = 0
                elif c == '-':
                    sign = -1
        if isNum:
            obj = NestedInteger()
            obj.setInteger(val * sign)
            ptr.add(obj)
        return ptr.getList()[0]


class CheatSolution:
    def deserialize(self, s: str) -> NestedInteger:
        return NestedInteger(s)


if __name__ == '__main__':
    for solution in [HonestSolution(), CheatSolution()]:
        print(solution.__class__.__name__ + ': ')
        print(solution.deserialize(s="324"))
        print(solution.deserialize(s="-3"))
        print(solution.deserialize(s="0"))
        print(solution.deserialize(s="[123,[456,[789]]]"))
        print(solution.deserialize(s='[-1,-2]'))
