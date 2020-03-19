import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = sys.maxsize
        mid = sys.maxsize
        for num in nums:
            if num < small:
                small = num
            elif num > small and num < mid:
                mid = num
            elif num > mid:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.increasingTriplet([1, 2, 3, 4, 5]) == True)
    print(solution.increasingTriplet([5, 4, 3, 2, 1]) == False)
    print(solution.increasingTriplet([2, 1, 5, 0, 4, 6]) == True)
    print(solution.increasingTriplet([1, 0, 2, 0, 3]) == True)
