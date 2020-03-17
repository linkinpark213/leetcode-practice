from typing import List


class Node:
    def __init__(self, v, distance, length):
        self.v = v
        self.distance = distance
        self.length = length

    def __gt__(self, other):
        return self.distance > other.distance

    def __lt__(self, other):
        return self.distance <= other.distance


class MinHeap:
    def __init__(self):
        self.l = []

    def _p(self, index):
        return (index - 1) // 2

    def _c(self, index):
        return index * 2 + 1

    def insert(self, v):
        self.l.append(v)
        ptr = len(self.l) - 1
        while ptr != 0 and self.l[ptr] < self.l[self._p(ptr)]:
            temp = self.l[ptr]
            self.l[ptr] = self.l[self._p(ptr)]
            self.l[self._p(ptr)] = temp
            ptr = self._p(ptr)

    def pop(self):
        first = self.l[0]
        last = self.l.pop()
        if len(self.l) > 0:
            self.l[0] = last
            ptr = 0
            while self._c(ptr) < len(self.l):
                if self.l[ptr] < self.l[self._c(ptr)] and (
                        self._c(ptr) + 1 == len(self.l) or self.l[ptr] < self.l[self._c(ptr) + 1]):
                    break
                elif self._c(ptr) + 1 == len(self.l) or self.l[self._c(ptr)] < self.l[self._c(ptr) + 1]:
                    temp = self.l[ptr]
                    self.l[ptr] = self.l[self._c(ptr)]
                    self.l[self._c(ptr)] = temp
                    ptr = self._c(ptr)
                elif self.l[self._c(ptr) + 1] < self.l[self._c(ptr)]:
                    temp = self.l[ptr]
                    self.l[ptr] = self.l[self._c(ptr) + 1]
                    self.l[self._c(ptr) + 1] = temp
                    ptr = self._c(ptr) + 1
        return first


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        queue = MinHeap()
        queue.insert(Node(src, 0, 0))
        distances = {}
        E = {i: [] for i in range(n)}
        for flight in flights:
            E[flight[0]].append((flight[1], flight[2]))

        while len(queue.l) > 0:
            node = queue.pop()
            if node.v == dst:
                if node.length <= K + 1:
                    return node.distance

            for v, dist in E[node.v]:
                if node.length <= K:
                    queue.insert(Node(v, node.distance + dist, node.length + 1))
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=1))
    print(solution.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=0))
    print(solution.findCheapestPrice(n=10, flights=[[3, 4, 4], [2, 5, 6], [4, 7, 10], [9, 6, 5], [7, 4, 4], [6, 2, 10],
                                                    [6, 8, 6],
                                                    [7, 9, 4], [1, 5, 4], [1, 0, 4], [9, 7, 3], [7, 0, 5], [6, 5, 8],
                                                    [1, 7, 6],
                                                    [4, 0, 9], [5, 9, 1], [8, 7, 3], [1, 2, 6], [4, 1, 5], [5, 2, 4],
                                                    [1, 9, 1],
                                                    [7, 8, 10], [0, 4, 2], [7, 2, 8]], src=6, dst=0, K=7))
    print(solution.findCheapestPrice(n=4, flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0, dst=3, K=1))
