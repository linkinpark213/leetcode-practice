from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = [root.val]
        viewLeft = self.rightSideView(root.left)
        viewRight = self.rightSideView(root.right)
        ans.extend(viewRight)
        if len(viewLeft) > len(viewRight):
            ans.extend(viewLeft[len(viewRight):])
        return ans


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(solution.rightSideView(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    print(solution.rightSideView(root))
