import sys
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        coins.reverse()
        self.minCoins = sys.maxsize

        def coinChangeHelper(coins, amount, coinsSpent):
            if amount == 0:
                self.minCoins = min(self.minCoins, coinsSpent)
                return

            if len(coins) == 0:
                return

            for num in range(amount // coins[0], -1, -1):
                if num + coinsSpent > self.minCoins:
                    break
                coinChangeHelper(coins[1:], amount - coins[0] * num, coinsSpent + num)

        coinChangeHelper(coins, amount, 0)
        return -1 if self.minCoins == sys.maxsize else self.minCoins


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))
    print(solution.coinChange([186, 419, 83, 408], 6249))
    print(solution.coinChange([3, 7, 405, 436], 8839))
