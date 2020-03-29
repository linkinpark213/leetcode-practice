class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self) -> str:
        s = str(self.val)
        if self.left is not None:
            s += '(' + self.left.__str__() + ', '
        else:
            s += '(None, '
        if self.right is not None:
            s += self.right.__str__() + ')'
        else:
            s += 'None)'
        s += '-> '
        s += str(self.next.val) if self.next is not None else 'None'
        return s


class PointerSolution:
    def connect(self, root: 'Node') -> 'Node':
        head = Node()
        head.next = root
        while head.next is not None:
            prevLayerPtr = head.next
            head.next = None
            newLayerPtr = head
            while prevLayerPtr is not None:
                for child in [prevLayerPtr.left, prevLayerPtr.right]:
                    if child is not None:
                        newLayerPtr.next = child
                        newLayerPtr = child
                prevLayerPtr = prevLayerPtr.next
        return root


class QueueSolution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        queue = [(0, root)]
        prev = (-1, None)
        while len(queue) > 0:
            depth, node = queue.pop(0)
            if node.left is not None:
                queue.append((depth + 1, node.left))
            if node.right is not None:
                queue.append((depth + 1, node.right))
            if prev[0] == depth:
                prev[1].next = node
            prev = (depth, node)

        return root


if __name__ == '__main__':
    for solution in [PointerSolution(), QueueSolution()]:
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.right = Node(7)
        print(solution.connect(root))

        root = Node(3)
        root.left = Node(9)
        root.right = Node(20)
        root.right.left = Node(15)
        root.right.right = Node(7)
        print(solution.connect(root))
