import sys
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dp = [[[sys.maxsize] * (k + 1) for __ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(k + 1):
            dp[-1][-1][i] = 0
        queue = [(len(grid) - 1, len(grid[0]) - 1)]
        while len(queue) > 0:
            i, j = queue.pop(0)
            for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if m >= 0 and n >= 0 and m < len(grid) and n < len(grid[0]):
                    updated = False
                    for stoneToClear in range(k + 1 - grid[m][n]):
                        if dp[m][n][stoneToClear + grid[m][n]] - 1 > dp[i][j][stoneToClear]:
                            updated = True
                            dp[m][n][stoneToClear + grid[m][n]] = dp[i][j][stoneToClear] + 1
                    if updated:
                        queue.append((m, n))

        minLength = min(dp[0][0])
        return minLength if minLength < len(grid) * len(grid[0]) else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPath(grid=
                                [[0, 0, 0],
                                 [1, 1, 0],
                                 [0, 0, 0],
                                 [0, 1, 1],
                                 [0, 0, 0]],
                                k=1))
    print(solution.shortestPath(grid=
                                [[0, 1, 1],
                                 [1, 1, 1],
                                 [1, 0, 0]],
                                k=1))
