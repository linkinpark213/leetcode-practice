class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ''
        ptr = self
        while ptr is not None:
            s += ' -> ' + str(ptr.val)
            ptr = ptr.next
        return s


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        while l1 is not None or l2 is not None:
            if l2 is None or (l1 is not None and l1.val <= l2.val):
                tail.next = l1
                l1 = l1.next
            elif l1 is None or (l2 is not None and l2.val <= l1.val):
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print(solution.mergeTwoLists(l1, l2))
