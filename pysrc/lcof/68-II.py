from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root is p or root is q:
            return root

        pathLeft = self.lowestCommonAncestor(root.left, p, q)
        pathRight = self.lowestCommonAncestor(root.right, p, q)
        if pathLeft is not None and pathRight is not None:
            return root
        elif pathRight is None:
            return pathLeft
        elif pathLeft is None:
            return pathRight


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    print(solution.lowestCommonAncestor(root, root.left, root.left.right.right))
