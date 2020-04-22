from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i + 1][j + 1] + 1, dp[i + 1][j] + 1, dp[i][j + 1] + 1)

        return max(max(line) for line in dp) ** 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximalSquare([['1', '0', '1', '0', '0'],
                                  ['1', '0', '1', '1', '1'],
                                  ['1', '1', '1', '1', '1'],
                                  ['1', '0', '0', '1', '0']]))
    print(solution.maximalSquare([['1', '0', '1', '0', '0'],
                                  ['1', '0', '1', '1', '1'],
                                  ['1', '1', '1', '1', '1'],
                                  ['1', '0', '0', '1', '0']]))
