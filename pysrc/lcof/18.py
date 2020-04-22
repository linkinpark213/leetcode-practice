class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ''
        ptr = self
        while ptr is not None:
            s += '->' + str(ptr.val)
            ptr = ptr.next
        return s


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        while ptr is not None and ptr.next is not None:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            ptr = ptr.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    print(solution.deleteNode(head=head, val=5))

    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    print(solution.deleteNode(head=head, val=1))

    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    print(solution.deleteNode(head=head, val=9))
