from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 3 for _ in range(2)]
        for i in range(n):
            for r in range(3):
                dp[i % 2][r] = max(dp[i % 2][r], dp[1 - i % 2][r])
                newR = (nums[i] + dp[1 - i % 2][r]) % 3
                dp[i % 2][newR] = max(dp[i % 2][newR], nums[i] + dp[1 - i % 2][r])

        return dp[1 - n % 2][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSumDivThree(nums=[3, 6, 5, 1, 8]) == 18)
    print(solution.maxSumDivThree(nums=[4]) == 0)
    print(solution.maxSumDivThree(nums=[1, 2, 3, 4, 4]) == 12)
