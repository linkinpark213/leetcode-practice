class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depthAndDiameter(self, node: TreeNode) -> tuple:
        depthLeft, diameterLeft = self.depthAndDiameter(node.left) if node.left is not None else (-1, -1)
        depthRight, diameterRight = self.depthAndDiameter(node.right) if node.right is not None else (-1, -1)
        return max(depthLeft, depthRight) + 1, max(depthLeft + depthRight + 2, diameterLeft, diameterRight)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.depthAndDiameter(root)[1] if root is not None else 0


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(solution.diameterOfBinaryTree(root))
    # print(solution.depthAndDiameter(root))
