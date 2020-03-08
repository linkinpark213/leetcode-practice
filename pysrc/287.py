from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def findDuplicateIn(nums: List[int], minimum: int, maximum: int) -> int:
            if (minimum == maximum):
                return minimum
            pivot = (minimum + maximum) // 2
            smallerCount = sum([1 for num in nums if num <= pivot and num >= minimum])
            biggerCount = sum([1 for num in nums if num > pivot and num <= maximum])
            if smallerCount > biggerCount:
                return findDuplicateIn(nums, minimum, pivot)
            else:
                return findDuplicateIn(nums, pivot + 1, maximum)

        return findDuplicateIn(nums, 1, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDuplicate([3, 1, 3, 4, 2]))
    print(solution.findDuplicate([1, 3, 4, 2, 1]))
