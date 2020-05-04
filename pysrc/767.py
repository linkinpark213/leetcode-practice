from typing import List


class Solution:
    def argsort(self, nums: List[int]) -> List[int]:
        nums = nums.copy()
        order = list(range(len(nums)))
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[j - 1]:
                    temp = nums[j]
                    nums[j] = nums[j - 1]
                    nums[j - 1] = temp
                    temp = order[j]
                    order[j] = order[j - 1]
                    order[j - 1] = temp
        return order

    def reorganizeString(self, S: str) -> str:
        counts = [0] * 26
        for c in S:
            counts[ord(c) - ord('a')] += 1
        if max(counts) > (len(S) + 1) // 2:
            return ''
        ans = [''] * len(S)
        pos = 0
        order = self.argsort(counts)
        for i in range(26):
            while counts[order[i]] > 0:
                ans[pos] = chr(order[i] + ord('a'))
                counts[order[i]] -= 1
                pos += 2
                if pos >= len(S):
                    pos = 1
        return ''.join(ans)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reorganizeString(S='aab'))
    print(solution.reorganizeString(S='aaab'))
    print(solution.reorganizeString(S='vvvlo'))
