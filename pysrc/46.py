from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        ans = []
        for num in nums:
            rest = nums.copy()
            rest.remove(num)
            subs = self.permute(rest)
            for sub in subs:
                sub.append(num)
                ans.append(sub)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute(nums=[1, 2, 3]))
