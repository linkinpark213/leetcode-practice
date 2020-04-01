from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        dp = [0, -prices[0]]
        for i in range(len(prices)):
            temp = dp[0]
            dp[0] = max(dp[0], dp[1] + prices[i] - fee)
            dp[1] = max(dp[1], temp - prices[i])

        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
    print(solution.maxProfit(prices=[4, 5, 2, 4, 3, 3, 1, 2, 5, 4], fee=1))
