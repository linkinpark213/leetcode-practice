class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queueP, queueQ = [p], [q]
        while len(queueP) > 0 and len(queueQ) > 0:
            p, q = queueP.pop(0), queueQ.pop(0)
            if ((p is None) ^ (q is None)) or (p and q and p.val != q.val):
                return False
            if p and q:
                queueP.append(p.left)
                queueP.append(p.right)
                queueQ.append(q.left)
                queueQ.append(q.right)
        return len(queueP) == 0 and len(queueQ) == 0


if __name__ == '__main__':
    solution = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(solution.isSameTree(p, q))

    q.left.left = TreeNode(4)
    print(solution.isSameTree(p, q))
