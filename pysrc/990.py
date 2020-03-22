from typing import List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.parent = self

    def ancestor(self):
        root = self
        while root != root.parent:
            root = root.parent
        prev = self
        ptr = self
        while ptr != ptr.parent:
            ptr = ptr.parent
            prev.parent = root
            prev = ptr
        return root

    def merge(self, other):
        self.ancestor().parent = other.ancestor()


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        V = [None] * 26
        stack = []
        for equation in equations:
            for var in [equation[0], equation[-1]]:
                if V[ord(var) - ord('a')] is None:
                    V[ord(var) - ord('a')] = Node(var)
            if equation[1:3] == '!=':
                stack.append((equation[0], equation[-1]))
            else:
                V[ord(equation[0]) - ord('a')].merge(V[ord(equation[-1]) - ord('a')])

        for var1, var2 in stack:
            if V[ord(var1) - ord('a')].ancestor() == V[ord(var2) - ord('a')].ancestor():
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.equationsPossible(["a==b", "b!=a"]))
    print(solution.equationsPossible(["b==a", "a==b"]))
    print(solution.equationsPossible(["a==b", "b==c", "a==c"]))
    print(solution.equationsPossible(["a==b", "b!=c", "c==a"]))
    print(solution.equationsPossible(["c==c", "b==d", "x!=z"]))
