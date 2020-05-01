from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def firstKLargest(self, root: TreeNode, k: int) -> List[int]:
        if root is None:
            return []
        ans = []
        ans.extend(self.firstKLargest(root.right, k))
        if len(ans) < k:
            ans.append(root.val)
        if len(ans) < k:
            ans.extend(self.firstKLargest(root.left, k - len(ans)))
        return ans

    def kthLargest(self, root: TreeNode, k: int) -> int:
        return self.firstKLargest(root, k)[-1]


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(solution.kthLargest(root=root, k=1))

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    print(solution.kthLargest(root=root, k=3))
