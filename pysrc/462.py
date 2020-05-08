from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        mids = [nums[n // 2]] if n % 2 == 1 else [nums[n // 2] - 1, nums[n // 2]]
        return min([sum([abs(num - mid) for num in nums]) for mid in mids])


if __name__ == '__main__':
    solution = Solution()
    print(solution.minMoves2([1, 2, 3]))
    print(solution.minMoves2([1, 0, 0, 8, 6]))
