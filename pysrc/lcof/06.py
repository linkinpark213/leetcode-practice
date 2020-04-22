from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        ptr = head
        while ptr is not None:
            ans.insert(0, ptr.val)
            ptr = ptr.next
        return ans


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    print(solution.reversePrint(head))
