class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def findNode(self, root: TreeNode, key: int):
        parent = None
        lr = 0
        ptr = root
        while ptr is not None:
            if ptr.val == key:
                return parent, ptr, lr
            elif ptr.val < key:
                parent = ptr
                lr = 1
                ptr = ptr.right
            elif ptr.val > key:
                parent = ptr
                lr = -1
                ptr = ptr.left
        return parent, ptr, lr

    def setChild(self, node: TreeNode, child: TreeNode, lr: int):
        if node is not None:
            if lr == 1:
                node.right = child
            elif lr == -1:
                node.left = child

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        parent, node, lr = self.findNode(root, key)
        if node is None:
            return root
        if node.left is None:
            self.setChild(parent, node.right, lr)
        if node.right is None:
            self.setChild(parent, node.left, lr)
        if node.left and node.right:
            self.setChild(parent, node.right, lr)
            ptr, _, __ = self.findNode(node.left, node.right.val)
            ptr.right = node.right.left
            node.right.left = node.left
        return root if node is not root else root.right if root.right is not None else root.left


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    print(solution.deleteNode(root, 3))

    root = TreeNode(0)
    print(solution.deleteNode(root, 0))
