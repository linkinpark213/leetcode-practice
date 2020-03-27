class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ''
        ptr = self
        while ptr is not None:
            s += str(ptr.val) + ', '
            ptr = ptr.next
        return s


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        fast = dummy
        slow = dummy
        i = 0
        while fast.next is not None:
            length += 1
            fast = fast.next
            i += 1
            if i > k:
                slow = slow.next

        if k % length == 0:
            return head
        elif length <= k:
            k = k % length
            for i in range(length - k):
                slow = slow.next

        dummy.next = slow.next
        fast.next = head
        slow.next = None

        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(solution.rotateRight(head, 2))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(solution.rotateRight(head, 8))

    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    print(solution.rotateRight(head, 4))

    head = ListNode(0)
    head.next = ListNode(1)
    print(solution.rotateRight(head, 2))
