# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while fast is not None and slow != fast:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            else:
                return False
            slow = slow.next

        if fast is None:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    print(solution.hasCycle(head))
