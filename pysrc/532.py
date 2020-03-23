from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            return len(set([num for num in nums if nums.count(num) > 1]))
        else:
            return len(set(nums) & set([num + k for num in nums]))


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPairs(nums=[3, 1, 4, 1, 5], k=2))
    print(solution.findPairs(nums=[1, 2, 3, 4, 5], k=1))
    print(solution.findPairs(nums=[1, 3, 1, 5, 4], k=0))
    print(solution.findPairs(
        nums=[2, 9, 0, 8, 9, 6, 5, 9, 8, 1, 9, 6, 9, 2, 8, 8, 7, 5, 7, 8, 8, 3, 7, 4, 1, 1, 6, 2, 9, 9, 3, 9, 2, 4, 6,
              5, 6, 5, 1, 5, 9, 9, 8, 1, 4, 3, 2, 8, 5, 3, 5, 4, 5, 7, 0, 0, 7, 6, 4, 7, 2, 4, 9, 3, 6, 6, 5, 0, 0, 0,
              8, 9, 9, 6, 5, 4, 6, 2, 1, 3, 2, 5, 0, 1, 4, 2, 6, 9, 5, 4, 9, 6, 0, 8, 3, 8, 0, 0, 2, 1], k=1))
