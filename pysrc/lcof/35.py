class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        s = ''
        ptr = self
        while ptr is not None:
            s += ' -> ' + str(ptr.val) + '( -> ' + (str(ptr.random.val) if ptr.random is not None else 'None') + ' )'
            ptr = ptr.next
        return s


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        ptr = head
        while ptr is not None:
            newNode = Node(ptr.val)
            newNode.next = ptr.next
            newNode.random = ptr.random
            ptr.next = newNode
            ptr = newNode.next

        ptr = head.next
        while ptr is not None:
            if ptr.random is not None:
                ptr.random = ptr.random.next
            ptr = ptr.next
            if ptr is None:
                break

        newHead = head.next
        ptr = head
        nptr = head.next
        while nptr.next is not None:
            ptr.next = ptr.next.next
            nptr.next = nptr.next.next
            ptr = ptr.next
            nptr = nptr.next
        return newHead


if __name__ == '__main__':
    solution = Solution()
    head = Node(7)
    head.next = Node(13)
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(1)
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head
    print(solution.copyRandomList(head))
