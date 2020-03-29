class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathcpy(self, path1, path2) -> int:
        ptr = 0
        while ptr < len(path1) and ptr < len(path2) and path1[ptr] == path2[ptr]:
            ptr += 1
        return len(path1) + len(path2) - ptr * 2

    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        pathTok = None
        leaves = []
        queue = [([], root)]
        while len(queue) > 0:
            path, node = queue.pop()
            if node.val == k:
                pathTok = path
            if node.left is None and node.right is None:
                leaves.append((path, node))
                continue
            if node.left is not None:
                queue.append((path + [0], node.left))
            if node.right is not None:
                queue.append((path + [1], node.right))

        closestPath = leaves[0][0]
        closestLeave = leaves[0][1]
        for path, node in leaves:
            if self.pathcpy(pathTok, path) < self.pathcpy(closestPath, pathTok):
                closestPath = path
                closestLeave = node

        return closestLeave.val


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    print(solution.findClosestLeaf(root, 1))

    root = TreeNode(1)
    print(solution.findClosestLeaf(root, 1))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    print(solution.findClosestLeaf(root, 2))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    root.right.left.left.left = TreeNode(8)
    root.right.left.left.right = TreeNode(9)
    root.right.right.right.left = TreeNode(10)
    print(solution.findClosestLeaf(root, 4))
