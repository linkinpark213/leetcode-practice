from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        x = nums[0]
        for i, num in enumerate(nums):
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1
        return x


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
