class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (len(s) > 0 and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))
        else:
            return len(s) > 0 and (s[0] == p[0] or p[0] == '.') and (self.isMatch(s[1:], p[1:]))


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch(s="aa", p="a"))
    print(solution.isMatch(s="aa", p="a*"))
    print(solution.isMatch(s="ab", p=".*"))
    print(solution.isMatch(s="aab", p="c*a*b"))
    print(solution.isMatch(s="mississippi", p="mis*is*p*."))
