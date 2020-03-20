from typing import List


class Solution:
    def makeEdge(self, nums: List[int], edgeLength: int) -> bool:
        if edgeLength == 0:
            return True
        for i, num in enumerate(nums):
            nums.pop(i)
            if edgeLength >= num and self.makeEdge(nums, edgeLength - num):
                return True
            nums.insert(i, num)

        return False

    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4 or sum(nums) % 4 != 0:
            return False
        edgeLength = sum(nums) // 4
        for i in range(3):
            nums.sort()
            nums.reverse()
            if not self.makeEdge(nums, edgeLength):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.makesquare([1, 1, 2, 2, 2]))
    print(solution.makesquare([3, 3, 3, 3, 4]))
    print(solution.makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]))
