from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        maxConsecutive = 0
        zeroCount = 0
        while right < len(nums):
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            if nums[right] == 0:
                zeroCount += 1
            right += 1
            if zeroCount <= 1:
                maxConsecutive = max(maxConsecutive, right - left)
        return maxConsecutive


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
    print(solution.findMaxConsecutiveOnes([1, 1, 0, 1]))
    print(solution.findMaxConsecutiveOnes([1]))
