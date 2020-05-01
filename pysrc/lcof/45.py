from typing import List


class Number:
    def __init__(self, num: int):
        self.val = num

    def __gt__(self, other):
        return int(str(self.val) + str(other.val)) > int(str(other.val) + str(self.val))


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = [Number(num) for num in nums]
        nums.sort()
        ans = ''
        for num in nums:
            ans += str(num.val)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.minNumber([10, 2]))
    print(solution.minNumber([12, 120]))
    print(solution.minNumber([12, 121]))
    print(solution.minNumber([12, 122]))
    print(solution.minNumber([12, 123]))
    print(solution.minNumber([3, 30, 34, 5, 9]))
