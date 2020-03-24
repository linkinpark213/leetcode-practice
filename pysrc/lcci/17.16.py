from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = [[0] * 2 for i in range(len(nums))]
        dp[0][1] = nums[0]
        dp[1][1] = nums[1]
        dp[1][0] = nums[0]
        for i in range(2, len(nums)):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = max(dp[i - 2]) + nums[i]
        return max(dp[-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.massage([1, 2, 3, 1]))
    print(solution.massage([2, 7, 9, 3, 1]))
    print(solution.massage([2, 1, 4, 5, 3, 1, 1, 3]))
