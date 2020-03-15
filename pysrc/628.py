from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumProduct([1, 2, 3, 4]))
