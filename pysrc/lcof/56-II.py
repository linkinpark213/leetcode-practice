from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            temp = (two & ~one & ~num) | (~two & one & num)
            one = (one ^ num) & ~two
            two = temp
        return one


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber(nums=[3, 4, 3, 3]))
    print(solution.singleNumber(nums=[9, 1, 7, 9, 7, 9, 7]))
