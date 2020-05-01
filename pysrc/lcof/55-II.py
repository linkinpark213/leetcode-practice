class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.isBalanced(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.right.right.left = TreeNode(4)
    root.right.right.right = TreeNode(4)
    print(solution.isBalanced(root))
