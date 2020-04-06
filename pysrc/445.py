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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        for l, s in [(l1, s1), (l2, s2)]:
            ptr = l
            while ptr is not None:
                s.append(ptr.val)
                ptr = ptr.next

        carry = 0
        node = None
        newNode = None
        while len(s1) > 0 or len(s2) > 0 or carry > 0:
            num1 = s1.pop() if len(s1) > 0 else 0
            num2 = s2.pop() if len(s2) > 0 else 0
            newNode = ListNode((num1 + num2 + carry) % 10)
            newNode.next = node
            node = newNode
            carry = (num1 + num2 + carry) // 10
        return newNode


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(solution.addTwoNumbers(l1, l2))
