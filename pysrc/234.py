class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        count = 0
        while fast is not None and slow.next is not None:
            slow.next.prev = slow
            slow = slow.next
            fast = fast.next
            count += 1
            if fast is not None:
                fast = fast.next
                count += 1
            else:
                slow = slow.prev
        l = slow
        r = slow if count % 2 == 0 else slow.next
        while r is not None:
            if l.val != r.val:
                return False
            r = r.next
            l = l.prev
        return True


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    print(solution.isPalindrome(head))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(solution.isPalindrome(head))
