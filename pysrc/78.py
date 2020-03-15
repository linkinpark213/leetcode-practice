from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = [[]]
        for num in nums:
            allSubsets = allSubsets + [subset + [num] for subset in allSubsets]
        return allSubsets


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
