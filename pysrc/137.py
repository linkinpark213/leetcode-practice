from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        twice = 0
        for num in nums:
            once = (once ^ num) & (~twice)
            twice = (twice ^ num) & (~once)
        return once


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2, 2, 3, 2]))
    print(solution.singleNumber([0, 1, 0, 1, 0, 1, 99]))
