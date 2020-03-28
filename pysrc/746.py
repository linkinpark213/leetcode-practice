from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        minCost = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            minCost.append(cost[i] + min(minCost[-1], minCost[-2]))

        return minCost[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs(cost=[10, 15, 20]))
    print(solution.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
