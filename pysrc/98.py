import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBSTWithBounds(self, root: TreeNode, lower: int, higher: int, anyLower: bool, anyHigher: bool) -> bool:
        if root is None:
            return True
        if anyHigher and root.val >= higher or anyLower and root.val <= lower:
            return False
        if root.left is not None:
            if not (root.left.val < root.val and self.isValidBSTWithBounds(root.left, lower, root.val, anyLower, True)):
                return False
        if root.right is not None:
            if not (root.right.val > root.val and self.isValidBSTWithBounds(root.right, root.val, higher, True,
                                                                            anyHigher)):
                return False
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTWithBounds(root, 0, 0, False, False)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    print(solution.isValidBST(root))

    root = TreeNode(-sys.maxsize - 1)
    root.right = TreeNode(sys.maxsize)
    root.right.left = TreeNode(-sys.maxsize)
    root.right.left = TreeNode(-sys.maxsize)
    print(solution.isValidBST(root))
