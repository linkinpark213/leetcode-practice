class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[n ** 2] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for j in range(n):
            for i in range(j - 1, -1, -1):
                dp[i][j] = min(i + 1 + dp[i + 1][j], j + 1 + dp[i][j - 1])
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], k + 1 + max(dp[i][k - 1], dp[k + 1][j]))
        return dp[0][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.getMoneyAmount(10))
    print(solution.getMoneyAmount(4))
