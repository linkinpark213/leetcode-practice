class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def findChildren(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if node is None:
            return None, None
        pParent, qParent = None, None
        if node.val == p.val:
            pParent = node
        if node.val == q.val:
            qParent = node
        for child in [node.left, node.right]:
            cp, cq = self.findChildren(child, p, q)
            if cp is not None:
                pParent = cp
            if cq is not None:
                qParent = cq

        if pParent is not None and qParent is not None and pParent is not qParent:
            return node, node

        return pParent, qParent

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node, _ = self.findChildren(root, p, q)
        return node


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    print(solution.lowestCommonAncestor(root, root.left, root.right))
    print(solution.lowestCommonAncestor(root, root.left, root.left.right.right))
