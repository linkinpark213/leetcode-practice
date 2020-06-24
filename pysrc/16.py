import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minDistance = sys.maxsize
        ans = 0
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                distance = abs(sum - target)
                if distance < minDistance:
                    ans = sum
                    minDistance = distance
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    return sum
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
