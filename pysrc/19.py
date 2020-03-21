class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ptr = self
        s = ''
        while ptr is not None:
            s += str(ptr.val) + ', '
            ptr = ptr.next
        return s

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        ptr1 = dummy
        ptr2 = dummy
        for i in range(n + 1):
            ptr1 = ptr1.next
        while ptr1 is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr2.next = ptr2.next.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(solution.removeNthFromEnd(head, 2))
