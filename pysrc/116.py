class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        s = str(self.val) + '('
        if self.left is not None:
            s += self.left.__str__() + ', '
        else:
            s += 'None, '
        if self.right is not None:
            s += self.right.__str__()
        else:
            s += 'None'
        s += ') -> '
        if self.next is not None:
            s += str(self.next.val)
        else:
            s += 'None'
        return s


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = Node()
        head.next = root
        while head.next is not None:
            prevPtr = head.next
            head.next = None
            newPtr = head
            while prevPtr is not None:
                for child in [prevPtr.left, prevPtr.right]:
                    if child is not None:
                        newPtr.next = child
                        newPtr = child
                prevPtr = prevPtr.next
        return root


if __name__ == '__main__':
    solution = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(solution.connect(root))
