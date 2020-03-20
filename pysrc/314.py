from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        nodeDict = {}
        stack = [(root, 0, 0)]
        while len(stack) > 0:
            node, x, y = stack.pop()
            if x not in nodeDict.keys():
                nodeDict[x] = []
            nodeDict[x].append((node, y))

            if node.right is not None:
                stack.append((node.right, x + 1, y + 1))
            if node.left is not None:
                stack.append((node.left, x - 1, y + 1))

        return [[ans[0].val for ans in sorted(nodeDict[x], key=lambda a: a[1])] for x in sorted(nodeDict.keys())]


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)
    root.left.right.right = TreeNode(2)
    root.right.left.left = TreeNode(5)
    print(solution.verticalOrder(root))
