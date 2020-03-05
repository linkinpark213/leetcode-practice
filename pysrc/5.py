class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalindromePos = 0
        maxPalindrome = 0
        for i in range(2 * len(s) - 1):
            palindrome = 1 - i % 2
            for j in range(1, min((i + 1) // 2 + 1, len(s) - i // 2)):
                if s[(i - 1) // 2 - j + 1] == s[i // 2 + j]:
                    palindrome += 2
                else:
                    break
            if palindrome > maxPalindrome:
                maxPalindrome = palindrome
                maxPalindromePos = i
        return s[(maxPalindromePos + 1) // 2 - maxPalindrome // 2: maxPalindromePos // 2 + maxPalindrome // 2 + 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('babad'))
    print(solution.longestPalindrome('cbbd'))
    print(solution.longestPalindrome('bb'))
    print(solution.longestPalindrome('abcda'))
