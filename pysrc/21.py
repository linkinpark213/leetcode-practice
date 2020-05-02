class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ptr = self
        s = ''
        while ptr is not None:
            s += ' -> ' + str(ptr.val)
            ptr = ptr.next
        return s


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(l2.val)
        dummy.next = l1
        ptr1, ptr2 = dummy, l2
        while ptr2 is not None:
            if ptr2.val >= ptr1.val and (ptr1.next is None or ptr1.next.val > ptr2.val):
                temp1, temp2 = ptr1.next, ptr2.next
                ptr1.next = ptr2
                ptr2.next = temp1
                ptr2 = temp2
            else:
                ptr1 = ptr1.next
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
