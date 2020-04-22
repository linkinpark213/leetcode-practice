from typing import List


class MinHeap:
    def __init__(self):
        self.list = []

    def _p(self, i):
        return (i - 1) // 2

    def _l(self, i):
        return i * 2 + 1

    def dist(self, point):
        return point[0] ** 2 + point[1] ** 2

    def swap(self, i, j):
        temp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = temp

    def push(self, element):
        self.list.append(element)
        ptr = len(self.list) - 1
        while ptr > 0:
            if self.dist(self.list[ptr]) < self.dist(self.list[self._p(ptr)]):
                self.swap(ptr, self._p(ptr))
                ptr = self._p(ptr)
            else:
                break

    def pop(self):
        item = self.list[0]
        self.list[0] = self.list[-1]
        self.list.pop()
        ptr = 0
        while self._l(ptr) < len(self.list):
            if self._l(ptr) < len(self.list) - 1 and self.dist(self.list[self._l(ptr) + 1]) < self.dist(
                    self.list[self._l(ptr)]) and self.dist(self.list[self._l(ptr) + 1]) < self.dist(self.list[ptr]):
                self.swap(ptr, self._l(ptr) + 1)
                ptr = self._l(ptr) + 1
            elif self.dist(self.list[self._l(ptr)]) < self.dist(self.list[ptr]):
                self.swap(ptr, self._l(ptr))
                ptr = self._l(ptr)
            else:
                break
        return item


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K >= len(points):
            return points

        heap = MinHeap()
        ans = []
        for point in points:
            heap.push(point)
        for i in range(K):
            ans.append(heap.pop())
        return ans


if __name__ == '__main__':
    solution = Solution()
    # print(solution.kClosest(points=[[1, 3], [-2, 2]], K=1))
    # print(solution.kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2))
    print(solution.kClosest(
        points=[[-95, 76], [17, 7], [-55, -58], [53, 20], [-69, -8], [-57, 87], [-2, -42], [-10, -87], [-36, -57],
                [97, -39], [97, 49]], K=5))
