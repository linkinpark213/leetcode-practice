from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        queues = [[root], []]
        ptr = 0
        while len(queues[0]) > 0 or len(queues[1]) > 0:
            ans.append([node.val for node in (queues[ptr] if ptr == 0 else reversed(queues[ptr]))])
            while len(queues[ptr]) > 0:
                node = queues[ptr].pop(0)
                if node.left is not None:
                    queues[1 - ptr].append(node.left)
                if node.right is not None:
                    queues[1 - ptr].append(node.right)
            ptr = 1 - ptr

        return ans


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.zigzagLevelOrder(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(solution.zigzagLevelOrder(root))
