from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if root is not None:
            for path in self.pathSum(root.left, sum - root.val):
                ans.append([root.val] + path)
            for path in self.pathSum(root.right, sum - root.val):
                ans.append([root.val] + path)
            if root.left is None and root.right is None and root.val == sum:
                return [[root.val]]
        return ans


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(solution.pathSum(root, 22))
