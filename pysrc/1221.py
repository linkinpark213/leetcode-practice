class Solution:
    def balancedStringSplit(self, s: str) -> int:
        curr = 0
        ans = 0
        for c in s:
            if c == 'R':
                curr += 1
            elif c == 'L':
                curr -= 1
            if curr == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.balancedStringSplit(s="RLRRLLRLRL"))
    print(solution.balancedStringSplit(s="RLLLLRRRLR"))
    print(solution.balancedStringSplit(s="LLLLRRRR"))
