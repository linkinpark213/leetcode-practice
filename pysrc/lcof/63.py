from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        low, profit = prices[0], 0
        for price in prices:
            profit = max(profit, price - low)
            low = min(low, price)
        return profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([7, 6, 4, 3, 1]))
