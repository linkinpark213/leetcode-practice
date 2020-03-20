from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            ans.append(node.val)
            if node.children is not None:
                for child in node.children:
                    stack.append(child)
        ans.reverse()
        return ans


if __name__ == '__main__':
    solution = Solution()
    root = Node(1, [Node(3), Node(2), Node(4)])
    root.children[0].children = [Node(5), Node(6)]
    print(solution.postorder(root))
