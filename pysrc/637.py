from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        ans = []
        queue = [(root, 0)]
        currentDepth, sum, count = -1, 0, 1
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if node is None:
                continue
            if depth != currentDepth:
                ans.append(sum / count)
                currentDepth, sum, count = depth, 0, 0

            sum, count = sum + node.val, count + 1
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        if count != 0:
            ans.append(sum / count)

        return ans[1:]


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.averageOfLevels(root))
