class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
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
