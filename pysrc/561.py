from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == '__main__':
    solution = Solution()
    print(solution.arrayPairSum([1, 4, 3, 2]))
