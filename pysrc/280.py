from typing import List


class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if ((i % 2) * 2 - 1) * (nums[i] - nums[i + 1]) < 0:
                self.swap(nums, i, i + 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.wiggleSort(nums=[1, 5, 1, 1, 6, 4]))
    print(solution.wiggleSort(nums=[1, 3, 2, 2, 3, 1]))
