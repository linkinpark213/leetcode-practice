from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
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
    print(solution.singleNumber([1, 2, 1, 3, 2, 5]))
    print(solution.singleNumber([-1, 0]))
