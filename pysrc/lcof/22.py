class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        for i in range(k):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(solution.getKthFromEnd(head, 2))
