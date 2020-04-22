from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        s = '(' + str(self.left) + ' <- '
        s += str(self.val) + ' -> '
        s += str(self.right) + ')'
        return s


class Solution:
    def buildTreeHelper(self, preorder: List[int], inorder: List[int], preRange: List[int],
                        inRange: List[int]) -> TreeNode:
        if preRange[0] >= preRange[1] or inRange[0] >= inRange[1]:
            return None
        rootVal = preorder[preRange[0]]
        root = TreeNode(rootVal)
        rootPos = inorder.index(rootVal, inRange[0], inRange[1])
        leftLen = rootPos - inRange[0]
        root.left = self.buildTreeHelper(preorder, inorder,
                                         [preRange[0] + 1, preRange[0] + leftLen + 1],
                                         [inRange[0], inRange[0] + leftLen])
        root.right = self.buildTreeHelper(preorder, inorder,
                                          [preRange[0] + leftLen + 1, preRange[1]],
                                          [inRange[0] + leftLen + 1, inRange[1]])
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildTreeHelper(preorder, inorder, [0, len(preorder)], [0, len(inorder)])


if __name__ == '__main__':
    solution = Solution()
    print(solution.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
