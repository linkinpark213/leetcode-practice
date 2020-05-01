class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ''
        ptr = self
        while ptr is not None:
            s += ' -> ' + str(ptr.val)
            ptr = ptr.next
        return s


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA, ptrB = headA, headB
        countA, countB = 0, 0
        while ptrA is not None:
            ptrA = ptrA.next
            countA += 1
        while ptrB is not None:
            ptrB = ptrB.next
            countB += 1

        if countA < countB:
            ptrA = headB
            ptrB = headA
        else:
            ptrA = headA
            ptrB = headB

        for i in range(abs(countA - countB)):
            ptrA = ptrA.next

        while ptrA is not None:
            if ptrA == ptrB:
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next
        return None


if __name__ == '__main__':
    solution = Solution()
    headA = ListNode(4)
    headA.next = ListNode(1)
    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = ListNode(1)
    headC = ListNode(8)
    headC.next = ListNode(4)
    headC.next.next = ListNode(5)
    headA.next.next = headC
    headB.next.next.next = headC
    print(solution.getIntersectionNode(headA, headB))

    headA = ListNode(2)
    headA.next = ListNode(6)
    headA.next.next = ListNode(4)
    headB = ListNode(1)
    headB.next = ListNode(5)
    print(solution.getIntersectionNode(headA, headB))
