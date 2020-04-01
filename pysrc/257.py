from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node: TreeNode, path: str) -> List[str]:
        if node is None:
            return [path[:-2]]
        ans = []
        path += str(node.val)
        if node.left is not None:
            ans.extend(self.dfs(node.left, path + '->'))
        if node.right is not None:
            ans.extend(self.dfs(node.right, path + '->'))
        if node.left is None and node.right is None:
            ans = [path]
        return ans

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        return self.dfs(root, '')


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print(solution.binaryTreePaths(root))
