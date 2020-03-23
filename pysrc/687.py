class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePathHelper(self, node: TreeNode) -> (int, int, int):
        if node is None:
            return 0, 0, 0

        longestIn, longestOut, longestAcross = 0, 0, 0
        nLeftIn, nLeftOut, nLeftAcross = self.longestUnivaluePathHelper(node.left)
        nRightIn, nRightOut, nRightAcross = self.longestUnivaluePathHelper(node.right)

        if node.left is not None:
            if node.val != node.left.val:
                longestOut = max(longestOut, nLeftIn, nLeftOut, nLeftAcross)
            else:
                longestIn = max(longestIn, nLeftIn + 1)
                longestOut = max(longestOut, nLeftOut, nLeftAcross)

        if node.right is not None:
            if node.val != node.right.val:
                longestOut = max(longestOut, nRightIn, nRightOut, nRightAcross)
            else:
                longestIn = max(longestIn, nRightIn + 1)
                longestOut = max(longestOut, nRightOut, nRightAcross)

        if node.left is not None and node.right is not None and node.val == node.left.val and node.val == node.right.val:
            longestAcross = nLeftIn + nRightIn + 2

        return longestIn, longestOut, longestAcross

    def longestUnivaluePath(self, root: TreeNode) -> int:
        return max(self.longestUnivaluePathHelper(root))


if __name__ == '__main__':
    solution = Solution()
    # root = TreeNode(5)
    # root.left = TreeNode(4)
    # root.right = TreeNode(5)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(1)
    # root.right.right = TreeNode(5)
    # print(solution.longestUnivaluePath(root))

    # root = TreeNode(1)
    # root.left = TreeNode(4)
    # root.right = TreeNode(5)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(4)
    # root.right.right = TreeNode(5)
    # print(solution.longestUnivaluePath(root))

    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(1)
    root.right.right.right = TreeNode(1)
    print(solution.longestUnivaluePath(root))
