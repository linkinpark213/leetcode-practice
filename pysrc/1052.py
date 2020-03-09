from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied = 0
        for i, customer in enumerate(customers):
            if grumpy[i] == 0:
                satisfied += customer

        maxSaved = 0
        for i in range(X):
            if grumpy[i] == 1:
                maxSaved += customers[i]

        saved = maxSaved
        for i in range(1, len(customers) - X + 1):
            if grumpy[i - 1] == 1:
                saved -= customers[i - 1]
            if grumpy[i + X - 1] == 1:
                saved += customers[i + X - 1]
            if saved > maxSaved:
                maxSaved = saved

        return satisfied + maxSaved


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
