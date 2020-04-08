class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        maxDepth = 0
        queue = [(1, root)]
        while len(queue) > 0:
            depth, node = queue.pop(0)
            if depth > maxDepth:
                maxDepth = depth
            if node.children is not None:
                for child in node.children:
                    queue.append((depth + 1, child))
        return maxDepth


if __name__ == '__main__':
    solution = Solution()
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    print(solution.maxDepth(root))
