from typing import List


class Solution:
    def permuteUniqueTuple(self, nums: List[int]):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [(nums[0],)]
        ans = set()
        for num in nums:
            rest = nums.copy()
            rest.remove(num)
            subs = self.permuteUniqueTuple(rest)
            for sub in subs:
                ans.add(tuple(list(sub) + [num]))
        return list(ans)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(t) for t in self.permuteUniqueTuple(nums)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))
