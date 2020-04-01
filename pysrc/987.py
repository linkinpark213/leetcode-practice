from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = {}
        queue = [(root, 0, 0)]
        while len(queue) > 0:
            node, x, y = queue.pop(0)
            if node is not None:
                if x not in d:
                    d[x] = {}
                if y not in d[x]:
                    d[x][y] = []
                d[x][y].append(node.val)
                queue.append((node.left, x - 1, y + 1))
                queue.append((node.right, x + 1, y + 1))
        ans = []
        for x in sorted(list(d.keys())):
            vals = []
            for y in sorted(d[x].keys()):
                vals.extend(sorted(d[x][y]))
            ans.append(vals)
        return ans


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.verticalTraversal(root))
