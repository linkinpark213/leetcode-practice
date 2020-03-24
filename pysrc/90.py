from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        freq = {}
        for num in nums:
            if num in freq.keys():
                freq[num] += 1
            else:
                freq[num] = 1
        for num in freq.keys():
            ans.extend([l + [num] * (i + 1) for l in ans for i in range(freq[num])])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([1, 2, 2]))
