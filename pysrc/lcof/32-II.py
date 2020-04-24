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
        queue = [(0, root)]
        vals = []
        while len(queue) > 0:
            depth, node = queue.pop(0)
            if node is not None:
                if len(vals) == depth:
                    vals.append([node.val])
                else:
                    vals[depth].append(node.val)
                queue.append((depth + 1, node.left))
                queue.append((depth + 1, node.right))
        return vals


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.levelOrder(root))
