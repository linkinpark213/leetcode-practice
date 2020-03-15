from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        tail = [0] * len(nums)
        maxLength = 0
        for num in nums:
            l, r = 0, maxLength
            while l < r:
                m = (l + r) // 2
                if tail[m] < num:
                    l = m + 1
                else:
                    r = m
            tail[l] = num
            if l == maxLength:
                maxLength += 1
        return maxLength


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
