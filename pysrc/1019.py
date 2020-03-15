from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nextLarger = []
        stack = []
        curr = head
        pos = 0
        while curr is not None:
            nextLarger.append(0)
            while len(stack) > 0 and curr.val > stack[-1][1]:
                p, _ = stack.pop()
                nextLarger[p] = curr.val
            stack.append((pos, curr.val))
            curr = curr.next
            pos += 1

        return nextLarger


def buildList(nums: List[int]):
    head = None
    ptr = None
    for num in nums:
        if ptr is None:
            ptr = ListNode(num)
            head = ptr
            continue
        ptr.next = ListNode(num)
        ptr = ptr.next
    return head


if __name__ == '__main__':
    solution = Solution()
    head = buildList([2, 1, 5])
    print(solution.nextLargerNodes(head))

    head = buildList([2, 7, 4, 3, 5])
    print(solution.nextLargerNodes(head))

    head = buildList([1, 7, 5, 1, 9, 2, 5, 1])
    print(solution.nextLargerNodes(head))
