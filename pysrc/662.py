class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = [(0, 0, root)]
        maxWidth = 0
        currentDepth = 0
        currentLeft = 0
        while len(queue) > 0:
            depth, x, node = queue.pop(0)
            if node is not None:
                if depth != currentDepth:
                    currentDepth = depth
                    currentLeft = x
                maxWidth = max(maxWidth, x - currentLeft + 1)
                queue.append((depth + 1, x * 2 + 1, node.left))
                queue.append((depth + 1, x * 2 + 2, node.right))

        return maxWidth


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    print(solution.widthOfBinaryTree(root))

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    print(solution.widthOfBinaryTree(root))

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    print(solution.widthOfBinaryTree(root))

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.right.right = TreeNode(9)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    print(solution.widthOfBinaryTree(root))
