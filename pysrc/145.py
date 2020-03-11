from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        out = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop(-1)
            out.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        out.reverse()
        return out


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(solution.postorderTraversal(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(solution.postorderTraversal(root))
