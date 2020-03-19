class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ptr = self
        s = '('
        while ptr is not None:
            s += str(ptr.val) + ', '
            ptr = ptr.next
        s += ')'
        return s


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    solution.deleteNode(head.next)
    print(head)
