from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        ptr = 0
        for i, c in enumerate(strs[0]):
            for s in strs:
                if len(s) <= i or c != s[i]:
                    return strs[0][:ptr]
            ptr += 1
        return strs[0][:ptr]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(['flower', 'flow', 'flight']))
