class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            temp = 0
            for j in range(i + 1):
                temp += dp[j] * dp[i - j - 1]
            dp[i] = temp
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(3))
    print(solution.numTrees(4))
