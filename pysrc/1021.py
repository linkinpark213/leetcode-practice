class Node:
    def __init__(self, parent):
        self.parent = parent
        self.children = []
        if parent is not None:
            self.parent.children.append(self)

    def toString(self):
        ans = ''
        for child in self.children:
            ans += child.toString()
        return ans if self.parent is None else '(' + ans + ')'

    def mergeChildren(self):
        breakable = True
        new_children = []
        for child in self.children:
            new_children.extend(child.children)
            if len(child.children) > 1:
                breakable = False
        self.children = new_children
        return breakable if len(self.children) > 0 else False


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        root = Node(None)
        node = root
        for c in S:
            if c == '(':
                node = Node(node)
            elif c == ')':
                node = node.parent

        root.mergeChildren()

        return root.toString()


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeOuterParentheses('(()())(())'))
    print(solution.removeOuterParentheses('(()())(())(()(()))'))
    print(solution.removeOuterParentheses('()()'))
    print(solution.removeOuterParentheses('(())'))
