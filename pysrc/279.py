class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))
        dp[0] = 0
        for i in range(n + 1):
            j = 1
            while j * j <= n:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(13))
