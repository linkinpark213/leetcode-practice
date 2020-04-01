from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        division = (n + 1) // 2
        nums.sort()
        smaller = nums[:division]
        bigger = nums[division:]
        nums[::2] = reversed(smaller)
        nums[1::2] = reversed(bigger)

if __name__ == '__main__':
    solution = Solution()
    print(solution.wiggleSort(nums=[1, 5, 1, 1, 6, 4]))
    print(solution.wiggleSort(nums=[1, 3, 2, 2, 3, 1]))
