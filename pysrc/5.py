class ForceSolution:
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


class ManacherSolution:
    def searchFrom(self, s: str, i: int, length: int) -> int:
        while i - length - 1 >= 0 and i + length + 1 < len(s) * 2 + 1:
            if (i - length - 1) % 2 == 0 or s[(i - length - 1) // 2] == s[(i + length + 1) // 2]:
                length += 1
            else:
                break
        return length

    def longestPalindrome(self, s: str) -> str:
        p = [0] * (2 * len(s) + 1)
        maxRight = 0
        center = 0
        for i in range(1, len(p)):
            if i > maxRight:
                radius = self.searchFrom(s, i, 0)
                p[i] = radius
                maxRight = i + radius
                center = i
            else:
                mirror = 2 * center - i
                if p[mirror] != maxRight - i:
                    p[i] = min(maxRight - i, p[mirror])
                else:
                    p[i] = self.searchFrom(s, i, maxRight - i)

        maxRadius = 0
        maxPos = 0
        for i, radius in enumerate(p):
            if radius > maxRadius:
                maxRadius = radius
                maxPos = i
        return s[(maxPos - maxRadius) // 2: (maxPos + maxRadius) // 2]


if __name__ == '__main__':
    for solution in [ForceSolution(), ManacherSolution()]:
        print(solution.longestPalindrome('babad'))
        print(solution.longestPalindrome('cbbd'))
        print(solution.longestPalindrome('bb'))
        print(solution.longestPalindrome('abcda'))
