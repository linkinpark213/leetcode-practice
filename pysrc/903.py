class Solution:
    mod = 10 ** 9 + 7

    def numPermsDISequence(self, S: str) -> int:
        n = len(S)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            if S[i - 1] == 'D':
                for j in range(0, i + 1):
                    dp[i][j] += sum(dp[i - 1][k] for k in range(j, i))
            elif S[i - 1] == 'I':
                for j in range(0, i + 1):
                    dp[i][j] += sum(dp[i - 1][k] for k in range(j))
        return sum(dp[n]) % self.mod


if __name__ == '__main__':
    solution = Solution()
    print(solution.numPermsDISequence('DID'))
