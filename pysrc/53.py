from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [0] * len(nums)
        for i, num in enumerate(nums):
            sums[i] = num + (sums[i - 1] if sums[i - 1] > 0 else 0)
        return max(sums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
