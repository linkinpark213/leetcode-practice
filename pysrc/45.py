from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        queue = [0]
        while len(queue) > 0:
            pos = queue.pop(0)
            for i in range(pos - nums[pos], pos + nums[pos] + 1):
                if i >= 0 and i < n and dp[i] > dp[pos] + 1:
                    dp[i] = dp[pos] + 1
                    queue.append(i)
                if i == n - 1:
                    return dp[i]

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.jump([2, 3, 1, 1, 4]))
    print(solution.jump(list(range(25000, -1, -1))))
