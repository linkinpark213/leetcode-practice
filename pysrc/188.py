import sys
from typing import List


class Solution:
    def maxProfitUnlimited(self, prices: List[int]) -> int:
        i = 1
        profit = 0
        while i < len(prices):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            i += 1
        return profit

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2 or k == 0:
            return 0
        if k >= len(prices) // 2:
            return self.maxProfitUnlimited(prices)
        dp = [[[-sys.maxsize] * 2 for __ in range(k + 1)] for _ in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0][0] = 0
            dp[i][1][1] = -prices[i]
            for t in range(k, 0, -1):
                dp[i][t][0] = max(dp[i - 1][t][1] + prices[i], dp[i - 1][t][0])
                dp[i][t][1] = max(dp[i - 1][t - 1][0] - prices[i], dp[i - 1][t][1])

        return max([line[0] for line in dp[-1]])


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(k=2, prices=[2, 4, 1]))
    print(solution.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
    print(solution.maxProfit(k=2, prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
