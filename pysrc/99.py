from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def midOrder(self, root: TreeNode) -> List[TreeNode]:
        if root is not None:
            return self.midOrder(root.left) + [root] + self.midOrder(root.right)
        return []

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        order = self.midOrder(root)

        i = 0
        while i < len(order) and order[i].val < order[i + 1].val:
            i = i + 1

        j = i + 1
        while j < len(order) and order[j].val < order[i].val:
            j = j + 1
        j = j - 1

        temp = order[i].val
        order[i].val = order[j].val
        order[j].val = temp
        return


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    print(solution.recoverTree(root))
