class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ''
        ptr = self
        while ptr is not None:
            s += '-' + str(ptr.val)
            ptr = ptr.next
        return s[1:]


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr = head
        prev = None
        while ptr is not None:
            if prev is not None and ptr.val == prev.val:
                prev.next = ptr.next
            else:
                prev = ptr
            ptr = ptr.next

        return head


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    print(solution.deleteDuplicates(head))

    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    print(solution.deleteDuplicates(head))
