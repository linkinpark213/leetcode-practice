class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = [(0, root)]
        count = 0
        while len(queue) > 0:
            num, node = queue.pop(0)
            if num != count:
                return False
            if node.left is not None:
                queue.append((num * 2 + 1, node.left))
            if node.right is not None:
                queue.append((num * 2 + 2, node.right))
            count += 1
        return True


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(solution.isCompleteTree(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(solution.isCompleteTree(root))
