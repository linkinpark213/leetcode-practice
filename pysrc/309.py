from typing import List


class Solution:
    def maxProfitHelper(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[1][1] = prices[1] - prices[0]
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0]) + prices[i] - prices[i - 1]
            
        return max(dp[-1][0], dp[-1][1])

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        return self.maxProfitHelper(prices)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 0, 2]))
    print(solution.maxProfit([2, 1, 2, 0, 1]))
    print(solution.maxProfit([6, 1, 3, 2, 4, 7]))
    print(solution.maxProfit([2, 1]))
    print(solution.maxProfit([1, 4, 2]))
    print(solution.maxProfit([2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8]))
    print(solution.maxProfit([8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]))
