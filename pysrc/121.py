from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_history = prices[0]
        max_profit = 0
        for price in prices[1:]:
            min_history = min(min_history, price)
            max_profit = max(max_profit, price - min_history)
        return max_profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([7, 6, 5, 4, 3]))
