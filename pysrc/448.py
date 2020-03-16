from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])

        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i + 1)

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
