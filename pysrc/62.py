class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                dp[j] += dp[j - 1] if j > 0 else 0
        return dp[n - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 2))
    print(solution.uniquePaths(7, 3))
