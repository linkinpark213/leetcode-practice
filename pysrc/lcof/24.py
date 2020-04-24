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
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr, next = None, head, head
        while next is not None:
            curr = next
            next = curr.next
            curr.next = prev
            prev = curr
        return curr


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(solution.reverseList(head))
