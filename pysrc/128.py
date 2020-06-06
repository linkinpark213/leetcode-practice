from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set()
        for num in nums:
            s.add(num)

        longest = 1
        for num in s:
            if not num - 1 in s:
                i = num + 1
                while i in s:
                    i += 1
                longest = max(longest, i - num)
        return longest


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
