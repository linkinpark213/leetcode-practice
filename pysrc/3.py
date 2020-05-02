class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        d = {}
        ans = 1
        while r < len(s):
            if s[r] not in d:
                d[s[r]] = r
                ans = max(ans, r - l + 1)
            else:
                while l < d[s[r]]:
                    d.pop(s[l])
                    l += 1
                l = d[s[r]] + 1
                d[s[r]] = r
            r += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
