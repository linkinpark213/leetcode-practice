from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        distance = [[-1] * len(grid[1]) for _ in range(len(grid))]
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    distance[i][j] = 0
                    queue.append((i, j, 0))
        maxDist = -1
        while len(queue) > 0:
            i, j, dist = queue.pop(0)
            for (m, n) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if m >= 0 and n >= 0 and m < len(grid) and n < len(grid[0]) and distance[m][n] == -1:
                    distance[m][n] = dist + 1
                    queue.append((m, n, dist + 1))
                    maxDist = max(maxDist, dist + 1)
        return -1 if maxDist <= 0 else maxDist


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDistance([[1, 0, 1],
                                [0, 0, 0],
                                [1, 0, 1]]))
    print(solution.maxDistance([[1, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]]))
