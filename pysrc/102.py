from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        currDepth = 0
        layer = []
        queue = [(root, 0)]
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if node is not None:
                if currDepth != depth:
                    if len(layer) > 0:
                        ans.append(layer)
                        layer = []
                    currDepth = depth
                layer.append(node.val)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        if len(layer) > 0:
            ans.append(layer)
        return ans


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.levelOrder(root))
