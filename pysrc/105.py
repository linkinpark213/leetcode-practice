from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + rootPos], inorder[:rootPos])
        root.right = self.buildTree(preorder[rootPos + 1:], inorder[rootPos + 1:])
        return root


if __name__ == '__main__':
    solution = Solution()
    root = solution.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
    print(root.val)
