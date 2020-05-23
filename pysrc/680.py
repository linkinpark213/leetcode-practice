class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return self.strictPalindrome(s[i:-i - 1]) or self.strictPalindrome(s[i + 1:len(s) - i])

        return True

    def strictPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.validPalindrome('aba'))
    print(solution.validPalindrome('abca'))
    print(solution.validPalindrome('abcda'))
    print(solution.validPalindrome('abc'))
