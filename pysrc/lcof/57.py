from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [nums[l], nums[r]]
            elif nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
    print(solution.twoSum(nums=[10, 26, 30, 31, 47, 60], target=40))
