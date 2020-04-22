class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class FindRepetitionSolution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        queue = [head]
        ptr = head
        while ptr is not None:
            ptr = ptr.next
            if ptr in queue:
                return ptr
            queue.append(ptr)
        return None


class DoublePointerSolution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if slow == fast:
                fast = dummy
                break

        while fast is not None:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return slow

        return None


if __name__ == '__main__':
    for solution in [FindRepetitionSolution(), DoublePointerSolution()]:
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = head.next
        print(solution.detectCycle(head))

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = head
        print(solution.detectCycle(head))

        head = ListNode(1)
        print(solution.detectCycle(head))
