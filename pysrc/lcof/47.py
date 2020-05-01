from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]
        for i in range(m - 1, - 1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = grid[i][j]
                if i < m - 1:
                    dp[i][j] = max(dp[i][j], grid[i][j] + dp[i + 1][j])
                if j < n - 1:
                    dp[i][j] = max(dp[i][j], grid[i][j] + dp[i][j + 1])
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxValue([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
