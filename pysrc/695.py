import time
from typing import List


class MapNode:
    def __init__(self):
        self.parent = self
        self.size = 1

    def ancestor(self):
        top = self
        while top.parent != top:
            top = top.parent

        prev = self
        ptr = self
        while ptr.parent != ptr:
            prev = ptr
            ptr = ptr.parent
            prev.parent = top
        return top

    def merge(self, node):
        if self.ancestor() != node.ancestor():
            node.ancestor().size += self.ancestor().size
            self.ancestor().parent = node.ancestor()


class UnionFindSolution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nodes = {}
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    node = MapNode()
                    nodes[(i, j)] = node
                    if (i - 1, j) in nodes.keys():
                        node.merge(nodes[(i - 1, j)])
                    if (i, j - 1) in nodes.keys():
                        node.merge(nodes[(i, j - 1)])

        return max([node.size for k, node in nodes.items()]) if len(nodes) != 0 else 0


class DFSSolution:
    def dfs(self, grid: List[List[int]], pos: List[int]) -> int:
        m, n = pos
        if m >= len(grid) or m < 0 or n >= len(grid[0]) or n < 0 or grid[m][n] == 0:
            return 0
        area = 1
        grid[m][n] = 0
        for (i, j) in [(m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1)]:
            area += self.dfs(grid, [i, j])
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    area = self.dfs(grid, [i, j])
                    if area > maxArea:
                        maxArea = area
        return maxArea


if __name__ == '__main__':
    for solution in [UnionFindSolution(), DFSSolution()]:
        startTime = time.time()
        print(solution.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))

        print(solution.maxAreaOfIsland([[1, 1, 0, 0, 0],
                                        [1, 1, 0, 0, 0],
                                        [0, 0, 0, 1, 1],
                                        [0, 0, 0, 1, 1]]))

        print(solution.maxAreaOfIsland([[0, 1],
                                        [1, 1]]))
        endTime = time.time()
        print('Time spent: {} s'.format(endTime - startTime))
