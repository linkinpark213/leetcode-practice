from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums) == 0:
            return 0
        dp = [{nums[0]: 1, -nums[0]: 1}] if nums[0] != 0 else [{0: 2}]
        for i in range(1, len(nums)):
            d = {}
            for k in dp[i - 1]:
                if k + nums[i] in d.keys():
                    d[k + nums[i]] += dp[i - 1][k]
                else:
                    d[k + nums[i]] = dp[i - 1][k]

                if k - nums[i] in d.keys():
                    d[k - nums[i]] += dp[i - 1][k]
                else:
                    d[k - nums[i]] = dp[i - 1][k]
            dp.append(d)

        return dp[-1][S] if S in dp[-1].keys() else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTargetSumWays(nums=[1, 1, 1, 1, 1], S=3))
    print(solution.findTargetSumWays(nums=[7, 46, 36, 49, 5, 34, 25, 39, 41, 38, 49, 47, 17, 11, 1, 41, 7, 16, 23, 13],
                                     S=3))
