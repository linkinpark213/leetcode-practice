from typing import List


class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max = nums[-1]
        i = len(nums) - 1
        while i >= 0:
            if nums[i] < max:
                break
            max = nums[i]
            i -= 1

        if i != -1:
            j = i + 1
            min = i + 1
            while j < len(nums):
                if nums[j] < nums[min] and nums[j] > nums[i]:
                    min = j
                j += 1
            self.swap(nums, i, min)

            for m in range(i + 1, len(nums)):
                for n in range(len(nums) - 1, m, -1):
                    if nums[n] < nums[n - 1]:
                        self.swap(nums, n, n - 1)
        else:
            nums.sort()


if __name__ == '__main__':
    solution = Solution()
    for nums in [[1, 2, 3], [3, 2, 1], [1, 1, 5], [1, 3, 2], [1, 2, 3, 5, 4, 1]]:
        solution.nextPermutation(nums)
        print(nums)
