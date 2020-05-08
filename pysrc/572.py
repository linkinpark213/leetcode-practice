class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode, startNow: bool = False) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val == t.val:
            if self.isSubtree(s.left, t.left, True) and self.isSubtree(s.right, t.right, True):
                return True
        return (not startNow) and self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == '__main__':
    solution = Solution()
    s = TreeNode(1)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    s.left.right.left = TreeNode(0)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    print(solution.isSubtree(s, t))
    t.right.left = TreeNode(0)
    print(solution.isSubtree(s, t))
