from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [0, 0]
        for i, num in enumerate(nums):
            temp = dp[0]
            dp[0] = max(dp)
            dp[1] = num + temp

        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1, 2, 3, 1]))
    print(solution.rob([2, 7, 9, 3, 1]))
