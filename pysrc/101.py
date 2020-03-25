# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isListSymmetric(self, l) -> bool:
        for i in range(len(l) // 2):
            if l[i] != l[-i - 1]:
                return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        queue = [(0, root)]
        layer = []
        currentDepth = 0
        while len(queue) > 0:
            depth, node = queue.pop(0)
            if currentDepth < depth:
                currentDepth = depth
                if not self.isListSymmetric(layer):
                    return False
                layer = []
            if node is None:
                layer.append(None)
            else:
                layer.append(node.val)
                queue.append((depth + 1, node.left))
                queue.append((depth + 1, node.right))

        return True


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(solution.isSymmetric(root) == True)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    print(solution.isSymmetric(root) == True)
