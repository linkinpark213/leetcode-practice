from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxLength = 0
        current = 0
        sums = [-1] * (len(nums) * 2)
        sums[0] = 0
        for i, num in enumerate(nums):
            current += 1 if num == 1 else -1
            if sums[current] >= 0:
                maxLength = max(maxLength, i - sums[current] + 1)
            else:
                sums[current] = i + 1
        return maxLength


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxLength([0, 1]))
    print(solution.findMaxLength([0, 1, 0]))
