class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ptr = self
        s = '('
        while ptr is not None:
            s += str(ptr.val) + ', '
            ptr = ptr.next

        s += ')'
        return s


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(m - 1):
            prev = prev.next
        next = prev
        for i in range(n - m + 2):
            next = next.next

        stack = []
        ptr = prev.next
        while ptr != next:
            stack.append(ptr)
            ptr = ptr.next
        ptr = prev
        while len(stack) > 0:
            node = stack.pop()
            ptr.next = node
            ptr = node
        ptr.next = next

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(solution.reverseBetween(head, 2, 4))
