from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArray = nums[-1]
        count = 0
        for num in nums:
            count += num
            if count > maxSubArray:
                maxSubArray = count
            if count < 0:
                count = 0
        return maxSubArray


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
