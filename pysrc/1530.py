from typing import List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def leavesAndPairs(self, node: TreeNode, distance: int) -> Tuple[List[int], int]:
        if node is None:
            return [], 0

        if node.left is None and node.right is None:
            return [0], 0

        leftLeaves, leftPairs = self.leavesAndPairs(node.left, distance)
        rightLeaves, rightPairs = self.leavesAndPairs(node.right, distance)
        leaves = leftLeaves + rightLeaves
        for i in range(len(leaves)):
            leaves[i] += 1
        pairs = leftPairs + rightPairs
        for leftLeave in leftLeaves:
            pairs += sum([1 for rightLeave in rightLeaves if rightLeave + leftLeave + 2 <= distance])

        return leaves, pairs

    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaves, pairs = self.leavesAndPairs(root, distance)
        return pairs


if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    print(solution.countPairs(root, 3) == 1)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(solution.countPairs(root, 3) == 2)

    root = TreeNode(7)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(3)
    root.right.left.left = TreeNode(2)
    print(solution.countPairs(root, 3) == 1)

    root = TreeNode(100)
    print(solution.countPairs(root, 1) == 0)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.countPairs(root, 2) == 1)
