from typing import List


class Solution:
    def printRemoveDuplicates(self, nums: List[int]) -> str:
        len = self.removeDuplicates(nums)
        ans = str(nums[:len])
        return ans

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        l, r = 0, 1
        val = nums[l]
        while r < len(nums):
            while r < len(nums) and val == nums[r]:
                r += 1
            if r < len(nums):
                val = nums[r]
                l += 1
                nums[l] = val

        return l + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.printRemoveDuplicates(nums=[1, 1, 2]))
    print(solution.printRemoveDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
