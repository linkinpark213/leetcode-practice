class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def areSymmetric(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None and B is None:
            return True
        elif A is None or B is None:
            return False
        return A.val == B.val and self.areSymmetric(A.left, B.right) and self.areSymmetric(A.right, B.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.areSymmetric(root.left, root.right)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(solution.isSymmetric(root))
