from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i != num:
                return i
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([0, 1, 3]))
    print(solution.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]))
