from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node: TreeNode) -> List[List[int]]:
        if node is None:
            return [[], []]
        ans = [[node.val], []]
        for child in [node.left, node.right]:
            pathsWithChild, pathsWithoutChild = self.dfs(child)
            ans[1].extend(pathsWithChild)
            ans[1].extend(pathsWithoutChild)
            for path in pathsWithChild:
                ans[0].append(node.val + path)

        return ans

    def pathSum(self, root: TreeNode, sum: int) -> int:
        pathsWithRoot, pathsWithoutRoot = self.dfs(root)
        return pathsWithRoot.count(sum) + pathsWithoutRoot.count(sum)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    print(solution.pathSum(root, 8))
