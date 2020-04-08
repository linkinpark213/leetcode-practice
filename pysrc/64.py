import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[sys.maxsize] * n for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + grid[i][j])
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + grid[i][j])

        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
