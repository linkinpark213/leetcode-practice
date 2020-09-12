from typing import List


class MaxHeap:
    def __init__(self):
        self.list = []

    def _p(self, i: int):
        return (i - 1) // 2

    def _l(self, i: int):
        return i * 2 + 1

    def _swap(self, i, j):
        temp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = temp

    def push(self, item):
        self.list.append(item)
        ptr = len(self.list) - 1
        while ptr > 0 and self.list[self._p(ptr)][1] < self.list[ptr][1]:
            self._swap(self._p(ptr), ptr)
            ptr = self._p(ptr)

    def pop(self):
        item = self.list[0]
        self._swap(0, len(self.list) - 1)
        self.list.pop()
        ptr = 0
        while self._l(ptr) < len(self.list):
            if self.list[ptr][1] > self.list[self._l(ptr)][1] and (
                    self._l(ptr) + 1 == len(self.list) or self.list[ptr][1] > self.list[self._l(ptr) + 1][1]):
                break
            elif self.list[ptr][1] < self.list[self._l(ptr)][1] and (
                    self._l(ptr) + 1 == len(self.list) or self.list[self._l(ptr)][1] > self.list[self._l(ptr) + 1][1]):
                self._swap(ptr, self._l(ptr))
                ptr = self._l(ptr)
            else:
                self._swap(ptr, self._l(ptr) + 1)
                ptr = self._l(ptr) + 1
        return item

    def top(self, minLeft: int):
        while self.list[0][0] < minLeft:
            self.pop()
        return self.list[0]


class HeapSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = MaxHeap()
        for i, num in enumerate(nums):
            heap.push((i, num))
            if i >= k - 1:
                ans.append(heap.top(i - k + 1)[1])
        return ans


class StackSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def push(stack, i, num):
            while len(stack) > 0 and stack[-1][1] <= num:
                stack.pop()
            stack.append((i, num))

        ans = []
        stack = []
        for i in range(k):
            push(stack, i, nums[i])
        ans.append(stack[0][1])

        for i in range(k, len(nums)):
            if stack[0][0] == i - k:
                stack.pop(0)
            push(stack, i, nums[i])
            ans.append(stack[0][1])

        return ans


if __name__ == '__main__':
    for solution in [HeapSolution(), StackSolution()]:
        print(solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
