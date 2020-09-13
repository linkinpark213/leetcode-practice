from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        lenAsc, lenDesc = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                lenAsc = lenDesc + 1
            elif nums[i] < nums[i - 1]:
                lenDesc = lenAsc + 1

        return max(lenAsc, lenDesc)


if __name__ == '__main__':
    solution = Solution()
    print(solution.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
    print(solution.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
    print(solution.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))
