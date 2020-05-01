class Solution:
    def firstUniqChar(self, s: str) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        for c in s:
            if freq[ord(c) - ord('a')] == 1:
                return c
        return ' '


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstUniqChar("abaccdeff"))
    print(solution.firstUniqChar(""))
