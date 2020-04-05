from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if reachable <= i + nums[i]:
                reachable = i
        return reachable == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump([2, 3, 1, 1, 4]))
    print(solution.canJump([3, 2, 1, 0, 4]))
