from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        a, b, c = 0, 0, 0
        for num in nums:
            a = a ^ num
        d = 1
        while a | d != a:
            d = d << 1

        for num in nums:
            if d | num == num:
                b = b ^ num
            else:
                c = c ^ num
        return [b, c]


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumbers(nums=[4, 1, 4, 6]))
    print(solution.singleNumbers(nums=[1, 2, 10, 4, 1, 4, 3, 3]))
