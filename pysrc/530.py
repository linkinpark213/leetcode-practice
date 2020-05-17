class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        l, q = [], [root]
        while len(q) > 0:
            node = q.pop(0)
            if node is not None:
                l.append(node.val)
                q.append(node.left)
                q.append(node.right)
        l.sort()
        diff = [abs(l[i] - l[i - 1]) for i in range(len(l))]
        return min(diff)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(solution.getMinimumDifference(root))
