class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = ''
        for c in s:
            ans += '%20' if c == ' ' else c
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.replaceSpace(s="We are happy."))
