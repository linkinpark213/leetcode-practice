from typing import List


class MinHeap:
    def __init__(self, capacity):
        self.list = []
        self.capacity = capacity
        self.sum = 0

    def _p(self, i):
        return (i - 1) // 2

    def _l(self, i):
        return i * 2 + 1

    def _swap(self, i, j):
        temp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = temp

    def push(self, element):
        self.sum += element
        self.list.append(element)
        ptr = len(self.list) - 1
        while ptr > 0:
            if self.list[self._p(ptr)] > self.list[ptr]:
                self._swap(self._p(ptr), ptr)
                ptr = self._p(ptr)
            else:
                break
        while len(self.list) > self.capacity:
            self.sum -= self.pop()

    def pop(self):
        top = self.list[0]
        self.list[0] = self.list[-1]
        self.list.pop()
        if len(self.list) > 0:
            ptr = 0
            while self._l(ptr) < len(self.list):
                if (self._l(ptr) == len(self.list) - 1 or self.list[self._l(ptr)] < self.list[self._l(ptr) + 1]) and \
                        self.list[self._l(ptr)] < self.list[ptr]:
                    self._swap(self._l(ptr), ptr)
                    ptr = self._l(ptr)
                elif self._l(ptr) < len(self.list) - 1 and self.list[self._l(ptr) + 1] < self.list[ptr]:
                    self._swap(self._l(ptr) + 1, ptr)
                    ptr = self._l(ptr) + 1
                else:
                    break
        return top


class Solution:
    mod = 10 ** 9 + 7

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        es = [(i, speed[i], efficiency[i]) for i in range(n)]
        es.sort(key=lambda x: x[2], reverse=True)
        heap = MinHeap(k - 1)

        best = 0
        for engineer in es:
            best = max(best, engineer[2] * (heap.sum + engineer[1]))
            heap.push(engineer[1])
        return best % self.mod


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2))
    print(solution.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=3))
    print(solution.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=4))
    print(solution.maxPerformance(n=7, speed=[1, 4, 1, 9, 4, 4, 4], efficiency=[8, 2, 1, 7, 1, 8, 4], k=6))
