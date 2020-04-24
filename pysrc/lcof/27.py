class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        temp = self.mirrorTree(root.left)
        root.left = self.mirrorTree(root.right)
        root.right = temp
        return root


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print(solution.mirrorTree(root))
