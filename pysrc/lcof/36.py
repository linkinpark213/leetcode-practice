class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def spanLeft(self, node: 'Node') -> 'Node':
        temp = node
        while node.right is not None:
            temp = node.right
            node.right = temp.left
            temp.left = node
            node = temp
        if temp.left is not None:
            temp.left = self.spanLeft(temp.left)
        return temp

    def spanRight(self, node: 'Node') -> 'Node':
        temp = node
        while node.left is not None:
            temp = node.left
            node.left = temp.right
            temp.right = node
            node = temp
        if temp.right is not None:
            temp.right = self.spanRight(temp.right)
        return temp

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        if root.left is not None:
            root.left = self.spanLeft(root.left)
        if root.right is not None:
            root.right = self.spanRight(root.right)
        left, right, temp = root, root, root
        while left.left is not None:
            left = left.left
            left.right = temp
            temp = left
        temp = root
        while right.right is not None:
            right = right.right
            right.left = temp
            temp = right
        left.left = right
        right.right = left
        return left


if __name__ == '__main__':
    solution = Solution()
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(solution.treeToDoublyList(root))
