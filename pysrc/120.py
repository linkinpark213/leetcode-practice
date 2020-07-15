import sys
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(i, -1, -1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j - 1])
        return min(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
