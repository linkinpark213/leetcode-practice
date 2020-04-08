from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 1:
                l += 1
            while l < r and nums[r] % 2 == 0:
                r -= 1
            if l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.exchange(nums=[1, 2, 3, 4]))
