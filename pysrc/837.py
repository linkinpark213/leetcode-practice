class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N > K + W - 1:
            return 1.0
        dp = [0.0] * (K + W)
        for i in range(K + W - 1, -1, -1):
            if i > N:
                dp[i] = 0.0
            elif i >= K:
                dp[i] = 1.0
            elif i == K - 1:
                dp[i] = sum([dp[j] for j in range(i + 1, i + W + 1)]) / W
            else:
                dp[i] = dp[i + 1] + dp[i + 1] / W - dp[i + W + 1] / W
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.new21Game(N=10, K=1, W=10))
    print(solution.new21Game(N=6, K=1, W=10))
    print(solution.new21Game(N=21, K=17, W=10))
