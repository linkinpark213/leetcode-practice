class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def isIdentical(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None and B is None:
            return True
        elif A is None:
            return False
        elif B is None:
            return True
        return A.val == B.val and self.isIdentical(A.left, B.left) and self.isIdentical(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False
        queue = [A]
        while len(queue) > 0:
            node = queue.pop(0)
            if node is not None:
                if node.val == B.val and self.isIdentical(node, B):
                    return True
                queue.append(node.left)
                queue.append(node.right)
        return False


if __name__ == '__main__':
    solution = Solution()
    A = TreeNode(3)
    A.left = TreeNode(4)
    A.right = TreeNode(5)
    A.left.left = TreeNode(1)
    A.left.right = TreeNode(2)
    B = TreeNode(4)
    B.left = TreeNode(1)
    print(solution.isSubStructure(A, B))
