# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ptr = self
        s = ''
        while ptr is not None:
            s += str(ptr.val)
            ptr = ptr.next
        return s


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        elif head.next.next is None:
            if head.val > head.next.val:
                temp = head.val
                head.val = head.next.val
                head.next.val = temp
            return head
        else:
            fast = head
            slow = head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                if fast is None:
                    break
                slow = slow.next
            l1 = head
            l2 = slow.next
            slow.next = None
            l1 = self.sortList(l1)
            l2 = self.sortList(l2)
            dummy = ListNode(0)
            ptr = dummy
            while l1 is not None or l2 is not None:
                if l2 is None or l1 is not None and l1.val < l2.val:
                    ptr.next = l1
                    l1 = l1.next
                else:
                    ptr.next = l2
                    l2 = l2.next
                ptr = ptr.next
                ptr.next = None
            return dummy.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    print(solution.sortList(head))
