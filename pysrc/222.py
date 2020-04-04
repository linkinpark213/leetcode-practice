class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        queue = [root]
        count = 0
        while len(queue) > 0:
            node = queue.pop()
            if node is not None:
                count += 1
                queue.append(node.left)
                queue.append(node.right)
        return count


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    print(solution.countNodes(root))
