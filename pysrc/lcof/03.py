from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
