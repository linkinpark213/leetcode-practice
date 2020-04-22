class Solution:
    def numWays(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numWays(n=2))
    print(solution.numWays(n=7))
