from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        zeros = nums.count(0)
        for i in range(max(nums), max(nums) - 5, -1):
            if i not in nums:
                if zeros > 0:
                    zeros -= 1
                else:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isStraight([1, 2, 3, 4, 5]))
    print(solution.isStraight([0, 0, 1, 2, 5]))
    print(solution.isStraight([0, 0, 1, 2, 6]))
