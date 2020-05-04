from typing import List


class Solution:
    def palindromeLength(self, s: str, i: int, minJ: int = 1):
        length = minJ - 1
        for j in range(minJ, min(i + 1, len(s) * 2 + 1 - i)):
            if (i + j) % 2 == 0 or s[(i + j) // 2] == s[(i - j) // 2]:
                length += 1
            else:
                break
        return length

    def palindromes(self, s: str) -> List[int]:
        ans = [0] * (len(s) + 1)
        maxRight, center = 0, 0
        for i in range(len(s) + 1):
            mirror = center * 2 - i
            if i >= maxRight or mirror - ans[mirror] == center * 2 - maxRight:
                ans[i] = self.palindromeLength(s, i, ans[mirror] if i < maxRight else 1)
                maxRight = i + ans[i]
                center = i
            else:
                ans[i] = min(maxRight - i, ans[mirror])
        print(ans)
        return ans

    def shortestPalindrome(self, s: str) -> str:
        center, maxLength = 0, 1
        palindromes = self.palindromes(s)
        for i, length in enumerate(palindromes[:len(s) + 1]):
            if i == length:
                maxLength = length
        prefix = list(reversed(list(s[maxLength:])))
        return ''.join(prefix) + s


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPalindrome('aacecaaa'))
    print(solution.shortestPalindrome('abcd'))
    print(solution.shortestPalindrome('a' * 100000))
    print(solution.shortestPalindrome('aabababababaababaa'))
