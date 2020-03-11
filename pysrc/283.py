from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sum = 0
        move = [0] * len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                sum += 1
                move[i] = len(nums) - sum
            else:
                move[i] = i - sum

        print('move: ', move)

        for i, num in enumerate(nums):
            if num != 0 and move[i] != i:
                nums[move[i]] = num
                nums[i] = 0


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)

    nums = [1]
    solution.moveZeroes(nums)
    print(nums)
