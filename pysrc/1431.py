from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [candy + extraCandies >= maxCandies for candy in candies]


if __name__ == '__main__':
    solution = Solution()
    print(solution.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
    print(solution.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
    print(solution.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
