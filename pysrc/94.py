from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    UNCHARTED = 0
    VISITED = 1

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [(self.UNCHARTED, root)]
        traversal = []
        while len(stack) != 0:
            state, node = stack.pop()
            if state == self.UNCHARTED:
                if node.right != None:
                    stack.append((self.UNCHARTED, node.right))
                stack.append((self.VISITED, node))
                if node.left != None:
                    stack.append((self.UNCHARTED, node.left))
            elif state == self.VISITED:
                traversal.append(node.val)
        return traversal


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(solution.inorderTraversal(root))
