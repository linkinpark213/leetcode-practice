class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        ptrA, ptrB = headA, headB
        while ptrA != ptrB:
            ptrA = headB if ptrA is None else ptrA.next
            ptrB = headA if ptrB is None else ptrB.next
        return ptrA


if __name__ == '__main__':
    solution = Solution()
    commonHead = ListNode(8)
    commonHead.next = ListNode(4)
    commonHead.next.next = ListNode(5)

    head1 = ListNode(4)
    head1.next = ListNode(1)
    head1.next.next = commonHead

    head2 = ListNode(5)
    head2.next = ListNode(0)
    head2.next.next = ListNode(1)
    head2.next.next.next = commonHead
    print(solution.getIntersectionNode(head1, head2).val)
