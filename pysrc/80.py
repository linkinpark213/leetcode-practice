from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        curr = 2
        while curr < len(nums):
            while curr < len(nums) and nums[curr - 2] == nums[curr] and nums[curr - 1] == nums[curr]:
                nums.pop(curr)
            curr += 1
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(solution.removeDuplicates(nums))
    print(nums)
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(solution.removeDuplicates(nums))
    print(nums)
